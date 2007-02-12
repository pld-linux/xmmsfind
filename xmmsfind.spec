Summary:	Playlist "jump to file" plugin for XMMS
Summary(pl.UTF-8):	Wtyczka do XMMS-a umożliwiająca skok do konkretnego pliku
Name:		xmmsfind
Version:	0.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/xmmsfind/%{name}-%{version}.tar.gz
# Source0-md5:	4b7de525ee8ac255a326ea729ae83cb4
URL:		http://xmmsfind.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small plugin for the X Multimedia System (xmms) that allows the user
to quickly search for and play a song in the current playlist! It can
be launched externally from the prompt or from a windowmanager
shortcut.

%description -l pl.UTF-8
Mała wtyczka do programu X Multimedia system (xmms), która umożliwia
użytkownikowi szybkie wyszukiwanie i odtwarzanie utworu z bieżącej
listy. Może być wywoływana zewnętrznie z powłoki lub ze skrótu
zarządcy okien.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{xmms_general_plugindir},%{_bindir}}

install libxmmsfind.so $RPM_BUILD_ROOT%{xmms_general_plugindir}
install remote/xmmsfind_remote $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO VERSION
%attr(755,root,root) %{xmms_general_plugindir}/*
%attr(755,root,root) %{_bindir}/*
