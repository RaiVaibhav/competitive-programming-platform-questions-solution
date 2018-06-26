def extract_wrapped(decorated):
    closure = (c.cell_contents for c in decorated.__closure__)
    return next((c for c in closure if isinstance(c, FunctionType)), None)


################################################################################
try:
    code = inspect.getsource(extract_wrapped(self.run))
except TypeError:
    code = inspect.getsource(self.run)
hoax_code = code[code.find('def'):]
print(hoax_code)
hoax_code = hoax_code.replace('run', 'hoax_method', 1)
exec(hoax_code, globals(), globals())
print(args)
prof = cProfile.Profile()
prof.enable()
hoax_method(self, *args, **kwargs)
prof.disable()
prof.print_stats()
