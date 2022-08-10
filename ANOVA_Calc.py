import math, os
from tabulate import tabulate

k = int(input("\nEnter the sample number of samples: "))
obs = int(input("\nEnter in the # of observations: "))
nT = k * obs
sample_dict, output_dict, sum_dict, mean_dict = {}, {}, {}, {}
SST, SSTr, SST1, SST2, SSE, MSTR, MSE, Fcalc, = 0, 0, 0, 0, 0, 0, 0, 0

array, mean = [], []

print("\n")

for i in range(1, (k + 1)):
    sample_dict[f"sample{i}"] = input("Enter the elements of sample " + str(i) + ": ").split()

for key, value in sample_dict.items():
    output_dict[key] = [float(item) for item in value]

for j in range(1, (k + 1)):
    sum_dict[f"sum{j}"] = sum(output_dict[f"sample{j}"])

for l in range(1, (k + 1)):
    mean_dict[f"mean{l}"] = (sum_dict.get(f"sum{l}")/obs)

total_mean = float(sum(mean_dict.values())/k)

os.system("cls")

for m in range(1, (k + 1)):
    print("The mean for", f"sample{m}", "=", mean_dict.get(f"mean{m}"))

for key,value in output_dict.items():
    array.append(value)

for key,value in mean_dict.items():
    mean.append(value)

for n in range(k):
    for o in range (obs):
        SST1 += (array[n][o])**2
        SST2 += array[n][o]

SST2 = (SST2**2)/nT

SST = SST1 - SST2

for q in range (k):
    SSTr += obs*((mean[q]) - total_mean)**2

SSE = (SST - SSTr)
MSTr = (SSTr / (k-1))
MSE = (SSE / (nT - k))
Fcalc = (MSTr / MSE)

print("\nThe total mean =", total_mean, "\n\nSST =", SST, "\n\nSSTr =", SSTr, "\n\nSSE =", SSE, "\n\nMSTr =", MSTr, "\n\nMSE =", MSE, "\n\nFcalc =", Fcalc, "\n\nd.o.f. 1 = ", k-1, "\n\nd.o.f. 2 = ", nT-k)

ANOVA = [["Model", k-1, SSTr, MSTr, Fcalc],
         ["Error", nT-k, SSE, MSE],
         ["Total", ((k-1)+(nT-k)), SSTr+SSE, MSTr+MSE]]        
headers=["Source", "d.o.f.", "SS", "MS", "Fcalc"]

print("\n")
print(tabulate(ANOVA, headers, tablefmt="pretty"))
input("\nPress ENTER to exit ")