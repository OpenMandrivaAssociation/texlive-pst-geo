%global tl_name pst-geo
%global tl_revision 79528

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.09a
Release:	%{tl_revision}.1
Summary:	Geographical Projections
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-geo
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-geo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-geo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a set of PSTricks related packages for various
cartographic projections of the terrestrial sphere. The package pst-
map2d provides conventional projections such as Mercator, Lambert,
cylindrical, etc. The package pst-map3d treats representation in three
dimensions of the terrestrial sphere. Packages pst-map2dII and pst-
map3dII allow use of the CIA World DataBank II. Various parameters of
the packages allow for choice of the level of the detail and the layouts
possible (cities, borders, rivers etc). Substantial data files are
provided, in an (internally) compressed format. Decompression happens
on-the-fly as a document using the data is displayed, printed or
converted to PDF format. A Perl script is provided for the user to do
the decompression, if the need should arise.

