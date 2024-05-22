#!/usr/bin/perl

use strict;
use warnings;

my $out_fname = 'out.sgi';

my $rgb_fname = 'output_rgba.raw';   # rgb channels from this file
my $RLE = 1;

my $W = 4000;
my $H = 5333;
my $FLAG1 = 'CHC{just_a_f4ke_flag}'; # In file name header
my $FLAG2 = "We're_No_Strangers_To_Love__You_Know_The_Rules_And_So_Do_I_(Do_I)__A_Full_Commitment's_What_I'm_Thinking_Of__You_Wouldn't_Get_This_From_Any_Other_Guy__I_Just_Wanna_Tell_You_How_I'm_Feeling__Gotta_Make_You_Understand__Never_Gonna_Give_You_Up__Never_Gonna_Let_You_Down__Never_Gonna_Run_Around_And_Desert_You__Never_Gonna_Make_You_Cry__Never_Gonna_Say_Goodbye__Never_Gonna_Tell_A_Lie_And_Hurt_You__ByeBye"; # In header padding

my $FLAG3 = 'CHC{REAL_FLAG_HERE}'; # In bytes between scan lines
warn 'Reading RGB data', "\n";
my $rgb_data;
open(my $INrgb, '<', $rgb_fname) or die 'Unable to open file: ', $rgb_fname, ' ', $!, "\n";
{
    local $/ = undef;
    $rgb_data  = <$INrgb>;
}
close($INrgb);

warn 'Splitting interlaced channels', "\n";
# split interlaced channels into distinct parts
my $chan_r = '';
my $chan_g = '';
my $chan_b = '';
my $chan_a = '';
for (my $y = 0; $y < $H; $y++) {
    for (my $x = 0; $x < $W; $x++) {
        $chan_r .= substr($rgb_data, (($x + ($y * $W)) * 4) + 0, 1);
        $chan_g .= substr($rgb_data, (($x + ($y * $W)) * 4) + 1, 1);
        $chan_b .= substr($rgb_data, (($x + ($y * $W)) * 4) + 2, 1);
        $chan_a .= substr($rgb_data, (($x + ($y * $W)) * 4) + 3, 1);
    }
}


my @sc_r = ();
my @sc_g = ();
my @sc_b = ();
my @sc_a = ();

warn 'Turning red channel into scanlines', "\n";
channel_to_scanlines($chan_r, \@sc_r);
warn 'Turning green channel into scanlines', "\n";
channel_to_scanlines($chan_g, \@sc_g);
warn 'Turning blue channel into scanlines', "\n";
channel_to_scanlines($chan_b, \@sc_b);
warn 'Turning alpha channel into scanlines', "\n";
channel_to_scanlines($chan_a, \@sc_a);



# The RLE scanline offset / length data
my $out_tot = 512 + ($H * 4 * 4 * 2); # Scanlines * channels * 4 bytes * 2 (offest + len)
my @sc_offset = ();
my @sc_len = ();

my $f4i = 0; # flag 4 index

warn 'Computing offest and length tables', "\n";
# R
for (my $i = 0; $i < $H; $i++) {
    my $l = length($sc_r[$i]);
    push @sc_offset, $out_tot;
    push @sc_len, $l;
    $out_tot += $l;

    # Hide flag 4 between red channel scanlines
    if ($f4i < length($FLAG3)) {
        $sc_r[$i] .= substr($FLAG3, $f4i, 1);
        $out_tot += 1;
        $f4i++;
    }
}

# G
for (my $i = 0; $i < $H; $i++) {
    my $l = length($sc_g[$i]);
    push @sc_offset, $out_tot;
    push @sc_len, $l;
    $out_tot += $l;
}

# B
for (my $i = 0; $i < $H; $i++) {
    my $l = length($sc_b[$i]);
    push @sc_offset, $out_tot;
    push @sc_len, $l;
    $out_tot += $l;
}
# A
for (my $i = 0; $i < $H; $i++) {
    my $l = length($sc_a[$i]);
    push @sc_offset, $out_tot;
    push @sc_len, $l;
    $out_tot += $l;
}


warn 'Writing image', "\n";


open(my $OUT, '>', $out_fname) or die 'Unable to open file for writing: ', $out_fname, ' ', $!, "\n";

warn 'Writing header', "\n";
print $OUT pack('nCCnnnnNNN', 474, (($RLE == 0)? 0 : 1), 1, 3, $W, $H, 4, 0, 255, 0);

# IMAGENAME
print $OUT $FLAG1;
print $OUT ("\0" x (80 - length($FLAG1)));

# COLORMAP
print $OUT pack('N', 0);

# DUMMY (padding)
print $OUT ($FLAG2);
print $OUT ("\xFF" x (404 - length($FLAG2)));

if ($RLE == 1) {
    warn 'Writing offest and len tables', "\n";
    print $OUT pack('N*', @sc_offset);
    print $OUT pack('N*', @sc_len);
}


warn 'Writing scanlines', "\n";

warn 'Red channel scanlines', "\n";
for (my $i = 0; $i < $H; $i++) {
    print $OUT $sc_r[$i];
}

warn 'Green channel scanlines', "\n";
for (my $i = 0; $i < $H; $i++) {
    print $OUT $sc_g[$i];
}

warn 'Blue channel scanlines', "\n";
for (my $i = 0; $i < $H; $i++) {
    print $OUT $sc_b[$i];
}
warn 'Alpha channel scanlines', "\n";
for (my $i = 0; $i < $H; $i++) {
    print $OUT $sc_a[$i];
}

close($OUT);



sub channel_to_scanlines {
    my $chan = shift;
    my $slref = shift;

    die sprintf('channel wrong size, got %d, expected %d, ', length($chan), $W * $H) unless (length($chan) == $W * $H);

    for (my $y = ($H - 1); $y >= 0; $y--) {
        my $chan_line = substr($chan, $y * $W, $W);

        if ($RLE == 1) {
            $chan_line = rle_sc($chan_line);
        }

        push @{$slref}, $chan_line;
    }
}
sub rle_sc {
    my $sc = shift;

    my @b = unpack('C*', $sc);

    my @rle_b = ();

    my $i = 0;
    my $c = 0;
    while ($i < $W) {
        my $l = runlen(\@b, $i);

        # clamp to max run length of 127
        if ($l > 127) {
            $l = 127;
        }

        push @rle_b, $l;
        push @rle_b, $b[$i];

        $c += $l;

        $i += $l;
    }
    push @rle_b, 0;

    if ($c != $W) {
        warn 'RLE encoded lengths wrong on scanline, got ', $c, ' expected ', $W, "\n";
    }

    return pack('C*', @rle_b);
}


sub runlen {
    my $bref = shift;
    my $o = shift;

    my $sc_len = scalar @{$bref};

    if ($sc_len <= $o) {
        return 0;
    }

    my $l = 1;
    my $b = $bref->[$o];
    for (my $i = $o + 1; $i < $sc_len; $i++) {
        if ($bref->[$i] == $b) {
            $l++;

            if ($l >= 127) {
                last;
            }
        } else {
            last;
        }
    }

    return $l;
}
