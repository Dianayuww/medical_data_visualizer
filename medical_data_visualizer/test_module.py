# test_module.py

import unittest
import pandas as pd
from medical_data_visualizer import df, draw_cat_plot, draw_heat_map


class DataVisualizerTests(unittest.TestCase):

    def test_overweight_column(self):
        # Hitung BMI = weight / (height in m)^2
        df_copy = df.copy()
        df_copy['height_m'] = df_copy['height'] / 100
        df_copy['bmi'] = df_copy['weight'] / (df_copy['height_m'] ** 2)
        df_copy['expected_overweight'] = (df_copy['bmi'] > 25).astype(int)

        self.assertTrue(
            (df_copy['overweight'] == df_copy['expected_overweight']).all(),
            msg="Overweight column calculated incorrectly."
        )

    def test_normalization(self):
        self.assertTrue(set(df['cholesterol'].unique()) <= {0, 1}, msg="Cholesterol not normalized correctly.")
        self.assertTrue(set(df['gluc'].unique()) <= {0, 1}, msg="Glucose not normalized correctly.")

    def test_cat_plot(self):
        fig = draw_cat_plot()
        axes = fig.axes
        self.assertEqual(len(axes), 2, msg="Expected 2 axes in the categorical plot (for cardio=0 and cardio=1).")

    def test_heatmap(self):
        fig = draw_heat_map()
        self.assertGreaterEqual(len(fig.axes), 1, msg="Expected at least 1 axis in the heatmap.")
        # Check if the heatmap contains a square matrix
        heatmap_data = fig.axes[0].collections[0].get_array()
        self.assertIsNotNone(heatmap_data, msg="Heatmap data is missing or incorrect.")


if __name__ == "__main__":
    unittest.main()
