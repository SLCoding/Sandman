    def check_install(self, check_name, legend, python=True, essential=False):
        """check wether needed tools are installed"""
        try:
            if python:
                find_module(check_name)
            else:
                pipe = subprocess.PIPE
                subprocess.Popen(check_name, stdout=pipe, stderr=pipe)

            return True
        except:
            if essential:
                self.log(legend, 3)
                exit()
                
                
                
                
                
                
python-utmp

self.check_install("Crypto", _("Install python-utmp to check for users logged in"))



TODO:
	func_critprocess auf leere strings prüfen