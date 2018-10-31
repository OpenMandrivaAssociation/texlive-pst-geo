Name:		texlive-pst-geo
Version:	0.06
Release:	2
Summary:	Geographical Projections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-geo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-geo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-geo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-geo is a set of PSTricks related packages for various
cartographic projections of the terrestrial sphere. The package
pst-map2d provides conventional projections such as Mercator,
Lambert, cylindrical, etc. The package pst-map3d treats
representation in three dimensions of the terrestrial sphere.
Packages pst-map2dII and pst-map3dII allow use of the CIA World
DataBank II. Various parameters of the packages allow for
choice of the level of the detail and the layouts possible
(cities, borders, rivers etc). Substantial data files are
provided, in an (internally) compressed format. Decompression
happens on-the-fly as a document using the data is displayed,
printed or converted to PDF format. A Perl script is provided
for the user to do the decompression, if the need should arise.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-geo
%{_texmfdistdir}/tex/generic/pst-geo
%{_texmfdistdir}/tex/latex/pst-geo
%doc %{_texmfdistdir}/doc/generic/pst-geo

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
