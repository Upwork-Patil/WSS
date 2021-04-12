I have added 3 functions:
get_fridays()
get_weekly_suppliment()
slice_tensor()
1. wss_id is a dict. read the dict and pass call appropriate function.
2. output of each function should be accumulated as consecutive dataframes
3. call --> slice_tensor(tensor frm step-2, [0, 2, 1], [data.shape[0], 1, 1])
4. plot, x-axis data_date, y-axis (values from step-3)


plotting basics


import matplotlib.pyplot as plt

plt.plot(x-axis, y-axis, lw=2)

plt.plot([1,2,3,4], [1,4,9,16], lw=2)

plt.show()
