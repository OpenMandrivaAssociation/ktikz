%define name	ktikz
%define version 0.11
%define rel	149
%define release %mkrel 0.svn%rel

Summary:	Program for creating diagrams with TikZ
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv3+
Group:		Graphics
Url:		http://www.hackenberger.at/ktikz/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tetex-latex, poppler
BuildRequires:	qt4-devel >= 4.6.0, qt4-assistant >= 4.6.0
BuildRequires:	libpoppler-qt4-devel
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

mkdir buildkde
pushd buildkde
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr ..
%make
popd

%install
%__rm -rf %{buildroot}

pushd buildqt
INSTALL_ROOT=%{buildroot} %make install 
popd
pushd buildkde
%make install 
rm -rf %{buildroot}%{_datadir}/mime/[agimstX]* %{buildroot}%{_datadir}/mime/text
popd

mv data/examples examples

chmod -R a+r Changelog LICENSE.* TODO examples/
chmod a+x examples

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog LICENSE.* TODO examples/
%{_bindir}/ktikz
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
%defattr(-,root,root)
%doc Changelog LICENSE.* TODO examples/
%{_bindir}/qtikz
%{_datadir}/qtikz/*
%{_datadir}/applications/qtikz.desktop
%{_datadir}/mime/packages/qtikz.xml
%{_mandir}/man1/qtikz.*
