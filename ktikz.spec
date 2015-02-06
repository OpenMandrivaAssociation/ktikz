%define name	ktikz

Summary:	Program for creating diagrams with TikZ
Name:		%{name}
Version:	0.11.0svn194
Release:	2
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		Graphics
Url:		http://www.hackenberger.at/ktikz/
Requires:	tetex-latex, poppler
BuildRequires:	qt4-devel >= 4.6.0, 
BuildRequires:	qt4-assistant >= 4.6.0
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	kdelibs4-devel

%description
KtikZ is a small KDE application for creating diagrams with TikZ.

%package -n qtikz
Summary:	Program for creating diagrams with TikZ
Group:		Graphics

%description -n qtikz
QtikZ is a small application for creating diagrams with TikZ.

%prep
%setup -q 

%build
sed -i -e 's,lrelease-qt4,lrelease,' qtikzconfig.pri
sed -i -e 's,\#MIME_INSTALL,MIME_INSTALL,' qtikzconfig.pri
sed -i -e 's,\/usr\/share\/mime\/packages,\$\$\{PREFIX\}\/share\/mime\/packages,' qtikzconfig.pri

mkdir buildqt
pushd buildqt
%qmake_qt4 ../qtikz.pro
%make
popd

%cmake_kde4
%make

%install
pushd buildqt
INSTALL_ROOT=%{buildroot} %make install 
popd
pushd build
%make DESTDIR=%{buildroot} install 
rm -rf %{buildroot}%{_datadir}/mime/[agimstX]* %{buildroot}%{_datadir}/mime/text
popd

mv data/examples examples

chmod -R a+r Changelog LICENSE.* TODO examples/
chmod a+x examples


%files
%doc Changelog LICENSE.* TODO examples/
%{_bindir}/ktikz
%{_libdir}/kde4/ktikz*so
%{_datadir}/config.kcfg/ktikz*
%{_datadir}/apps/ktikz*/*
%{_datadir}/applications/kde4/ktikz.desktop
%{_datadir}/kde4/services/ktikz*.desktop
%{_datadir}/doc/*
%{_iconsdir}/*/*/*/ktikz.*
%{_datadir}/locale/*/*/ktikz.mo
%{_datadir}/mime/packages/ktikz.xml
%{_mandir}/man1/ktikz.*

%files -n qtikz
%doc Changelog LICENSE.* TODO examples/
%{_bindir}/qtikz
%{_datadir}/qtikz/*
%{_datadir}/applications/qtikz.desktop
%{_datadir}/mime/packages/qtikz.xml
%{_mandir}/man1/qtikz.*


