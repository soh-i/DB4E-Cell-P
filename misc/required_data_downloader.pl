#!/usr/bin/env perl

use strict;
use warnings;
use LWP::Simple;

my $required_data = {
                     "TerminatorSet.txt" => "http://regulondb.ccg.unam.mx/menu/download/datasets/files/TerminatorSet.txt",
                     "PromoterSet.txt" => "http://regulondb.ccg.unam.mx/menu/download/datasets/files/PromoterSet.txt",
                    };

for my $file (keys $required_data) {
    _downloader($required_data->{$file}, $file)
}

sub _downloader {
    my $url = shift;
    my $out_file_name = shift;
    
    my $content = get($url);
    open my $fh, '>', $out_file_name or die "Can not open file:$!";
    print $fh $content;
    close $fh;
}

    
    
