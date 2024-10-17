Name:		texlive-chemformula
Version:	61719
Release:	2
Summary:	Command for typesetting chemical formulas and reactions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemformula
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemformula.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemformula.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a command to typeset chemical formulas and
reactions in support of other chemistry packages (such as
chemmacros). The package used to be distributed as a part of
chemmacros.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chemformula
%doc %{_texmfdistdir}/doc/latex/chemformula

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
