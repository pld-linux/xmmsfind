Summary:	Playlist "jump to file" plugin for XMMS
Summary(pl):	Wtyczka do XMMSa umo¿liwiaj±ca skok do konkretnego pliku
Name:		xmmsfind
Version:	0.4.7
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6f8b005d4bd9a31f7137893495e48c11
URL:		X11/Applications/Sound
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define _xmms_plugin_dir %{_libdir}/xmms

%description
A small plugin for the X Multimedia System (xmms) that allows the user
to quickly search for and play a song in the current playlist! It can
be launched externally from the prompt or from a windowmanager
shortcut.

%description -l pl
Ma³a wtyczka do programu X Multimedia system (xmms) która umo¿liwia
u¿ytkownikowi szybkie wyszukiwanie i odtwarzanie utworu z bie¿±cej
listy. Mo¿e byæ wywo³ywany zewnêtrznie z pow³oki lub ze skrótu
menad¿era okien.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xmms_plugin_dir}/General,%{_bindir}}

install libxmmsfind.so $RPM_BUILD_ROOT%{_xmms_plugin_dir}/General
install remote/xmmsfind_remote $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO VERSION
%attr(755,root,root) %{_xmms_plugin_dir}/General/*
%attr(755,root,root) %{_bindir}/*
