# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Maq(AutotoolsPackage):
    """Maq is a software that builds mapping assemblies from short reads
    generated by the next-generation sequencing machines."""

    homepage = "https://maq.sourceforge.net/"
    url = "https://downloads.sourceforge.net/project/maq/maq/0.7.1/maq-0.7.1.tar.bz2"
    list_url = "https://sourceforge.net/projects/maq/files/maq/"
    maintainers("snehring")

    license("GPL-3.0-only")

    version("0.7.1", sha256="e1671e0408b0895f5ab943839ee8f28747cf5f55dc64032c7469b133202b6de2")
    version("0.5.0", sha256="c292c19baf291b2415b460d687d43a71ece00a7d178cc5984bc8fc30cfce2dfb")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("perl", type="run")

    def patch(self):
        with working_dir("scripts"):
            scripts = ["farm-run.pl", "maq_eval.pl", "maq.pl", "maq_plot.pl"]
            for s in scripts:
                filter_file("/usr/bin/perl", self.spec["perl"].prefix.bin.perl, s)

    def flag_handler(self, name, flags):
        if name.lower() == "cxxflags":
            flags.append("-fpermissive")
        return (flags, None, None)
