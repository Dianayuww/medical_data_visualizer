# main.py

import medical_data_visualizer

# Menampilkan categorical plot
cat_plot_fig = medical_data_visualizer.draw_cat_plot()
cat_plot_fig.savefig('catplot.png')
cat_plot_fig.show()

# Menampilkan heatmap
heat_map_fig = medical_data_visualizer.draw_heat_map()
heat_map_fig.savefig('heatmap.png')
heat_map_fig.show()
