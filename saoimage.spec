Summary:	SAOimage - displays astronomical images on X11 Window System
Summary(pl):	SAOimage - program wy¶wietlaj±cy obrazy astronomiczne pod X11 Window System
Name:		saoimage
Version:	1.31.1
Release:	2
License:	Free, only Copyright must be preserved
Group:		X11/Applications/Graphics
Source0:	ftp://cfa-ftp.harvard.edu/pub/gsc/SAOimage/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://tdc-www.harvard.edu/software/saoimage.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SAOimage is a program which displays astronomical images on the X11
Window system. It can display FITS and IRAF .imh as well as binary
images of a size and data type specified on the command line.

%description -l pl
SAOimage to program do wy¶wietlania obrazów astronomicznych pod X11
Window System. Mo¿e wy¶wietlaæ formaty FITS i IRAF .imh, a tak¿e
binarne obrazy o rozmiarze i typie danych podanych z linii poleceñ.

%prep
%setup -q
%patch -p1

%build
%{__make} linux \
	CC="%{__cc}" \
	OFLAGS="%{rpmcflags}"

cd doc
dvips manual.dvi -o manual.ps

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/dev,%{_sysconfdir}}

%{__make} install -f makefile.linux \
	ROOT=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/dev/imt1
ln -sf imt1o $RPM_BUILD_ROOT/dev/imt1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README doc/*.{txt,ps,code}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/imtoolrc
%attr(666,root,root) /dev/imt*
