Name:		texlive-statex2
Version:	23961
Release:	2
Summary:	Statistics style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/statex2
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/statex2.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines many macros for items of significance in
statistical presentations. It represents a syntax-incompatible
upgrade of statex.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/statex2/statex2.sty
%doc %{_texmfdistdir}/doc/latex/statex2/statex2-example.pdf
%doc %{_texmfdistdir}/doc/latex/statex2/statex2-example.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
