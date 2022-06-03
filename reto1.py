sistolica = int(input())
diastolica = int(input())
if sistolica < 72 and diastolica < 65:
    print('Hipotension alerta Amarilla')
elif (sistolica >= 72 and sistolica < 107) and (diastolica >= 65 and diastolica < 73):
    print('Optima alerta Verde')
elif (sistolica >= 107 and sistolica < 124) and (diastolica >= 73 and diastolica < 81):
    print('Normal alerta Verde')
elif (sistolica >= 124 and sistolica < 138) and (diastolica >= 81 and diastolica < 93):
    print('Prehipertencion alerta Amarilla')
elif (sistolica >= 138 and sistolica < 156) and (diastolica >= 93 and diastolica < 102):
    print('HTA Grado1 alerta Naranja')
elif (sistolica >= 156 and sistolica < 175) and (diastolica >= 102 and diastolica < 114):
    print('HTA Grado2 alerta Roja')
elif (sistolica >= 175) and (diastolica >= 114):
    print('HTA Grado3 alerta Roja')
elif (sistolica >= 138) and diastolica < 92:
    print('Hipertension Sistolica Aislada alerta Naranja')  
else:
    print('No se puede determinar la categoria Alerta Gris')