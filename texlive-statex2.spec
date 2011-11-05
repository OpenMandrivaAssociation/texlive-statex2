# revision 23961
# category Package
# catalog-ctan /macros/latex/contrib/statex2
# catalog-date 2011-09-14 18:03:50 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-statex2
Version:	2.1
Release:	1
Summary:	Statistics style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/statex2
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex2.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines many macros for items of significance in
statistical presentations. It represents a syntax-incompatible
upgrade of statex.

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
%{_texmfdistdir}/tex/latex/statex2/statex2.sty
%doc %{_texmfdistdir}/doc/latex/statex2/statex2-example.pdf
%doc %{_texmfdistdir}/doc/latex/statex2/statex2-example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
