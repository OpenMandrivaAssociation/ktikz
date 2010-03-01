%define name	ktikz
%define version 0.9
%define rel	70
%define release %mkrel 0.svn%rel

Summary:	Program for creating diagrams with TikZ
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Graphics
Url:		http://www.hackenberger.at/ktikz/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	tetex-latex, poppler
BuildRequires:	qt4-devel
BuildRequires:	libpoppler-qt4-devel

%description
KtikZ is a small application for creating diagrams with TikZ.

%prep
%setup -q

%build
sed -i -e 's,PREFIX = \/usr,PREFIX = %{buildroot}\/usr,' conf.pri
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
%make install 

cat > %{buildroot}%_datadir/applications/ktikz.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=KTikZ
Exec=ktikz
Icon=/usr/share/ktikz/ktikz-128.png
DocPath=
Terminal=false
MimeType=text/x-pgf;text/x-tex;
Categories=Qt;KDE;Office;
GenericName=TikZ editor
GenericName[fr]=Éditeur TikZ
Comment=Program for creating TikZ (from the LaTeX pgf package) diagrams
Comment[fr]=Programme pour créer des diagrammes TikZ (du paquet LaTeX pgf)
EOF
chmod -R a+r Changelog LICENSE.* TODO examples/ debian/ktikz.1
chmod a+x examples

%__install -d -m 755 %{buildroot}%{_mandir}/man1/
%__install -m 644 debian/ktikz.1 %{buildroot}%{_mandir}/man1/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog LICENSE.* TODO examples/
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.*
