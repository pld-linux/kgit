Summary:	KDE frontend for GIT repositories
Summary(pl.UTF-8):	Interfejs do zarządzania repozytoriami GIT dla KDE
Name:		kgit
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kgit/%{name}-%{version}.tar.bz2
# Source0-md5:	adef4a6ca7a9da22b86ef9d30ce6ec97
URL:		http://kgit.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	git-core
Requires:	kdelibs >= 3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small but functional frontend to the popular source control program,
git. It is similar to 'gitk' with two significant differences:
- written in Qt using KDevelop and KDE libraries,
- it is functional unlike gitk which is only a repository viewer.

%description -l pl.UTF-8
Mały, ale funkcjonalny interfejs do popularnego systemu kontroli
źródeł - gita. Jest podobny do 'gitk' z dwiema znaczącymi różnicami:
- jest napisany przy pomocy bibliotek Qt i KDE w KDevelopie,
- jest funkcjonalny w przeciwieństwie do 'gitk', który jest tylko
przeglądarką repozytoriów.

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kgit.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kgit
%attr(755,root,root) %{_bindir}/kgit_client
%{_datadir}/apps/kgit
%{_desktopdir}/kde/kgit.desktop
%{_iconsdir}/hicolor/*/apps/kgit.png
