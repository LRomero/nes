#!/usr/bin/perl

# ------------------------------------------------------------------------------
#
#  NES by - Skriptke
#  Copyright 2009 - 2010 Enrique F. Castañón
#  Licensed under the GNU GPL.
#  http://sourceforge.net/projects/nes/
# 
#  Version 0.9 pre
#
#  latest_comments.cgi 
#
# ------------------------------------------------------------------------------

use Nes;
# Creamos un objeto de la clase Singleton
my $nes = Nes::Singleton->new();

# comentario para generar un enlace en "Ver fuente" a lib.cgi: ../scripts/lib.cgi
require 'lib.cgi';

# en %tags vamos a guardar los valores que posteriormente le pasaremos a $nes en el método out
my $nes_tags = {};

my $lang = $ENV{'PATH_INFO'};
$lang =~ s/.*\/(..)\/[^\/]*/$1/;

$nes_tags->{'lang'}    = $lang;

# por último mostramos la página pasandole los datos en el método out
$nes->out(%$nes_tags);

# importante que devuelvan 1 para evitar un error "couldn't run"
1;
