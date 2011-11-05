# revision 17751
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-geo
# catalog-date 2009-08-31 11:47:07 +0200
# catalog-license lppl
# catalog-version 2.03
Name:		texlive-pst-geo
Version:	2.03
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-geo/pst-map3d.pro
%{_texmfdistdir}/dvips/pst-geo/pst-map3dII.pro
%{_texmfdistdir}/tex/generic/pst-geo/data/README
%{_texmfdistdir}/tex/generic/pst-geo/data/aus.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/c-cap.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/c-sub.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/canada.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/capitales.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/capitales3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/capitals.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/cities.data
%{_texmfdistdir}/tex/generic/pst-geo/data/cities.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/citycapitals.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/citysub.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/convert.py
%{_texmfdistdir}/tex/generic/pst-geo/data/corse.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/france.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/mex.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/pborder.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/pcoast.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/pisland.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/plake.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/rhone.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/ridge.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/river.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/seine.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/transfrm.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/trench.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/usa.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/villesFrance.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/villesFrance3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/villesItalia.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/villesItalia3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/data/wfraczon.dat
%{_texmfdistdir}/tex/generic/pst-geo/data/wmaglin.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/README
%{_texmfdistdir}/tex/generic/pst-geo/dataII/africa-bdy.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/africa-cil.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/africa-riv.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/asia-bdy.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/asia-cil.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/asia-isl.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/asia-riv.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/c-cap.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/c-sub.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/citycapitals.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/citysub.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/europe-bdy.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/europe-cil.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/europe-riv.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/namer-bdy.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/namer-cil.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/namer-pby.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/namer-riv.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/samer-arc.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/samer-bdy.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/samer-cil.dat
%{_texmfdistdir}/tex/generic/pst-geo/dataII/samer-riv.dat
%{_texmfdistdir}/tex/generic/pst-geo/pst-map2d.tex
%{_texmfdistdir}/tex/generic/pst-geo/pst-map2dII.tex
%{_texmfdistdir}/tex/generic/pst-geo/pst-map3d.tex
%{_texmfdistdir}/tex/generic/pst-geo/pst-map3dII.tex
%{_texmfdistdir}/tex/latex/pst-geo/pst-map2d.sty
%{_texmfdistdir}/tex/latex/pst-geo/pst-map2dII.sty
%{_texmfdistdir}/tex/latex/pst-geo/pst-map3d.sty
%{_texmfdistdir}/tex/latex/pst-geo/pst-map3dII.sty
%doc %{_texmfdistdir}/doc/generic/pst-geo/Changes
%doc %{_texmfdistdir}/doc/generic/pst-geo/PSTricks.bib
%doc %{_texmfdistdir}/doc/generic/pst-geo/README
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-geo-compress.pl
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-geo-decompress.pl
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map2d-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map2d-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map2dII-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map2dII-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map3d-doc-pdf.pdf
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map3d-doc-pdf.tex
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map3d-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map3d-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map3dII-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-geo/pst-map3dII-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
