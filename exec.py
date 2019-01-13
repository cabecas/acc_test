import future
import acc as acc
import fun
import importdata as imp
import reg as reg
import matplotlib.pyplot as plt

# executing acc.py file
def exec():


    # NOTA: Antes de correr o ficheiro Excel, abrir o ficheiro e ir a:
    # Ficheiro->Informações->Verificar a Existência de Problemas->
    # Inspeccionar Documento->Inspeccionar

    mat = imp.read_file('pH412.test', 'Folha4')
    clean = acc.cleaning(mat, analise='pH')
    slopes = acc.declive(clean, window=100)
    t, pH = acc.selecting(slopes, slopes=2, fraction=1/4,
                  target_slope1=0.02, target_slope2=0.001, shift=50)

    all_pulses = acc.breaking(t, pH)
    all_pulses = acc.breaking2(all_pulses, pulsos=5,
                               set_point=1)
    acc.plotting(all_pulses)

    list = reg.return_parameter(profile = all_pulses, parameter = 'k')
    plt.figure()
    reg.plot_parameter(list)

    return

if __name__ == '__main__':
    exec()


# executing acc.py & future_work file

mat = imp.read_file('pH412.test', 'Folha4')
clean = acc.cleaning(mat, analise='pH')
slopes = acc.declive(clean, window=100)
maxim = future.indices(slopes, cut_value=1.5,
                       pulse_size=600)
t, pH = future.selecting_entire_pulse(slopes, maxim)
all_pulses = acc.breaking(t, pH)
all_pulses = acc.breaking2(all_pulses, pulsos=5,
                           set_point=1)
acc.plotting(all_pulses)

