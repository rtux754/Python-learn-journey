# casting data
print('\nCASTING DATA\n')

# integer
print("\n===INTEGER===\n")

int_ = 45

float_ = float(int_)
print("data = ",float_,"type = ",type(float_))

str_ = str(int_)
print("data = ",str_,"type = ",type(str_))

bool_= bool(int_)
print('data = ',bool_,'type = ',type(bool_))

# float
print('\n===FLOAT===\n')

flt = 6.9

init = int(flt)
print('data = ',init,'type = ',type(init))

strm = str(flt)
print('data = ',strm,'type = ',type(strm))

bole = bool(flt)
print('data = ',bole,'type = ',type(bole))

#string
print('\n===STRING===\n')

stri = "12" # data integer dan data float hanya bisa merubah string jika nilai string adalah variabel

itg =  int(stri) 
print('data = ',itg,'type = ',type(itg))

flt = float(stri)
print('data = ',flt,'type = ',type(flt))

blh = bool(stri)
print('data = ',blh,'type = ',type(blh))

#boolean
print('\n===BOOLEAN===\n')

boleh = True

inter = int(boleh)
print('data = ',inter,'type = ',type(inter))

flat = float(boleh)
print('data = ',flat,'type = ',type(flat))

stng = str(boleh)
print('data = ',stng,'type = ',type(stng))