%global tl_name chemformula
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.17
Release:	%{tl_revision}.1
Summary:	Command for typesetting chemical formulas and reactions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemformula
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemformula.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemformula.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(units)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a command to typeset chemical formulas and
reactions in support of other chemistry packages (such as chemmacros).
The package used to be distributed as a part of chemmacros.

