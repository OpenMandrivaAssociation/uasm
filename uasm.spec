%undefine _debugsource_packages

Name: uasm
Version: 2.56.2
Release: 1
Source0: https://github.com/Terraspace/uasm/archive/refs/tags/v%{version}.tar.gz
Patch0: uasm-2.56.2-clang.patch
Summary: MASM compatible assembler
URL: https://www.terraspace.co.uk/uasm.html
License: Watcom-1.0
Group: Development/Tools

%description
UASM is a free MASM-compatible assembler based on JWasm with these features:

* native support for output formats Intel OMF, MS Coff (32/64-bit),
  Elf (32/64-bit), Binary, Windows PE (32/64-bit) and DOS MZ.
* Instructions up to AVX2 and AVX512F are supported including all
  new extensions for VMX, MPX, AES, BND, F16C etc.
* Support for MS Vectorcall on x64.
* Support for Borland Register Calling Convention.
* Full support for SystemV Calling Convention.
* Integrated Macro Library with OO support.
* Numerous new HLL features (as described in the extended manual).
* UASM is written in C. The source is portable and has successfully been
  tested with Open Watcom, MS VC, GCC and more.
* C header files can be converted to include files for UASM with h2incX.
* UASM's source code is released under the Sybase Open Watcom Public License,
  which allows free commercial and non-commercial use.

JWasm started as a fork of Open Watcom's Wasm in March 2008. Today, the part
of Wasm source lines still contained in JWasm is approximately 15%.
UASM is a continued evolution of JWasm.

%prep
%autosetup -p1 -n UASM-%{version}

%build
%make_build -f gccLinux64.mak CC="%{__cc}" CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install GccUnixR/%{name} -t %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
%license License.txt
