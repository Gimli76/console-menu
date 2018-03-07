from __future__ import print_function

from unittest import TestCase

from consolemenu.format import AsciiBorderStyle, LightBorderStyle, HeavyBorderStyle, DoubleLineBorderStyle
from consolemenu.format.menu_borders import *


class TestAsciiBorderStyle(TestCase):

    def test(self):
        border = AsciiBorderStyle()
        # print(border.bottom_left_corner)
        # print(border.bottom_right_corner)
        # print(border.top_left_corner)
        # print(border.top_right_corner)
        # print(border.outer_horizontal)
        # print(border.outer_horizontal_inner_down)
        # print(border.outer_horizontal_inner_up)
        # print(border.outer_vertical)
        # print(border.outer_vertical_inner_left)
        # print(border.outer_vertical_inner_right)

        self.assertEqual('+', border.bottom_left_corner)
        self.assertEqual('+', border.bottom_right_corner)
        self.assertEqual('+', border.top_left_corner)
        self.assertEqual('+', border.top_right_corner)
        self.assertEqual('-', border.outer_horizontal)
        self.assertEqual('+', border.outer_horizontal_inner_down)
        self.assertEqual('+', border.outer_horizontal_inner_up)
        self.assertEqual('|', border.outer_vertical)
        self.assertEqual('|', border.outer_vertical_inner_left)
        self.assertEqual('|', border.outer_vertical_inner_right)


class TestLightBorderStyle(TestCase):

    def test(self):
        border = LightBorderStyle()
        # print border.bottom_left_corner
        # print border.bottom_right_corner
        # print border.top_left_corner
        # print border.top_right_corner
        # print border.outer_horizontal
        # print border.outer_horizontal_inner_down
        # print border.outer_horizontal_inner_up
        # print border.outer_vertical
        # print border.outer_vertical_inner_left
        # print border.outer_vertical_inner_right

        self.assertEqual(u'\u2514', border.bottom_left_corner)
        self.assertEqual(u'\u2518', border.bottom_right_corner)
        self.assertEqual(u'\u250C', border.top_left_corner)
        self.assertEqual(u'\u2510', border.top_right_corner)
        self.assertEqual(u'\u2500', border.outer_horizontal)
        self.assertEqual(u'\u252C', border.outer_horizontal_inner_down)
        self.assertEqual(u'\u2534', border.outer_horizontal_inner_up)
        self.assertEqual(u'\u2502', border.outer_vertical)
        self.assertEqual(u'\u2524', border.outer_vertical_inner_left)
        self.assertEqual(u'\u251C', border.outer_vertical_inner_right)


class TestHeavyBorderStyle(TestCase):

    def test(self):
        border = HeavyBorderStyle()
        # print(border.bottom_left_corner)
        # print(border.bottom_right_corner)
        # print(border.top_left_corner)
        # print(border.top_right_corner)
        # print(border.outer_horizontal)
        # print(border.outer_horizontal_inner_down)
        # print(border.outer_horizontal_inner_up)
        # print(border.outer_vertical)
        # print(border.outer_vertical_inner_left)
        # print(border.outer_vertical_inner_right)

        self.assertEqual(u'\u2517', border.bottom_left_corner)
        self.assertEqual(u'\u251B', border.bottom_right_corner)
        self.assertEqual(u'\u2501', border.inner_horizontal)
        self.assertEqual(u'\u2503', border.inner_vertical)
        self.assertEqual(u'\u254B', border.intersection)
        self.assertEqual(u'\u2501', border.outer_horizontal)
        self.assertEqual(u'\u2533', border.outer_horizontal_inner_down)
        self.assertEqual(u'\u253B', border.outer_horizontal_inner_up)
        self.assertEqual(u'\u2503', border.outer_vertical)
        self.assertEqual(u'\u2520', border.outer_vertical_inner_left)
        self.assertEqual(u'\u252B', border.outer_vertical_inner_right)
        self.assertEqual(u'\u250F', border.top_left_corner)
        self.assertEqual(u'\u2513', border.top_right_corner)


class TestDoubleLineBorderStyle(TestCase):

    def test(self):
        border = DoubleLineBorderStyle()
        # print(border.bottom_left_corner)
        # print(border.bottom_right_corner)
        # print(border.top_left_corner)
        # print(border.top_right_corner)
        # print(border.outer_horizontal)
        # print(border.outer_horizontal_inner_down)
        # print(border.outer_horizontal_inner_up)
        # print(border.outer_vertical)
        # print(border.outer_vertical_inner_left)
        # print(border.outer_vertical_inner_right)

        self.assertEqual(u'\u255A', border.bottom_left_corner)
        self.assertEqual(u'\u255D', border.bottom_right_corner)
        self.assertEqual(u'\u2550', border.inner_horizontal)
        self.assertEqual(u'\u2551', border.inner_vertical)
        self.assertEqual(u'\u256C', border.intersection)
        self.assertEqual(u'\u2550', border.outer_horizontal)
        self.assertEqual(u'\u2566', border.outer_horizontal_inner_down)
        self.assertEqual(u'\u2569', border.outer_horizontal_inner_up)
        self.assertEqual(u'\u2551', border.outer_vertical)
        self.assertEqual(u'\u2563', border.outer_vertical_inner_left)
        self.assertEqual(u'\u2560', border.outer_vertical_inner_right)
        self.assertEqual(u'\u2554', border.top_left_corner)
        self.assertEqual(u'\u2557', border.top_right_corner)


class TestMenuBorderStyleType(TestCase):

    def test(self):
        self.assertEqual(0, MenuBorderStyleType.ASCII_BORDER)
        self.assertEqual(1, MenuBorderStyleType.LIGHT_BORDER)
        self.assertEqual(2, MenuBorderStyleType.HEAVY_BORDER)
        self.assertEqual(3, MenuBorderStyleType.DOUBLE_LINE_BORDER)


class TestMenuBorderFactory(TestCase):

    def test_create_ascii_border(self):
        style = MenuBorderStyleFactory().create_ascii_border()
        self.assertTrue(isinstance(style, AsciiBorderStyle))

    def test_create_light_border(self):
        style = MenuBorderStyleFactory().create_light_border()
        self.assertTrue(isinstance(style, LightBorderStyle))

    def test_create_heavy_border(self):
        style = MenuBorderStyleFactory().create_heavy_border()
        self.assertTrue(isinstance(style, HeavyBorderStyle))

    def test_create_doubleline_border(self):
        style = MenuBorderStyleFactory().create_doubleline_border()
        self.assertTrue(isinstance(style, DoubleLineBorderStyle))

    def test_create_border(self):
        style = MenuBorderStyleFactory().create_border(MenuBorderStyleType.ASCII_BORDER)
        self.assertTrue(isinstance(style, AsciiBorderStyle))

        style = MenuBorderStyleFactory().create_border(MenuBorderStyleType.LIGHT_BORDER)
        self.assertTrue(isinstance(style, LightBorderStyle))

        style = MenuBorderStyleFactory().create_border(MenuBorderStyleType.HEAVY_BORDER)
        self.assertTrue(isinstance(style, HeavyBorderStyle))

        style = MenuBorderStyleFactory().create_border(MenuBorderStyleType.DOUBLE_LINE_BORDER)
        self.assertTrue(isinstance(style, DoubleLineBorderStyle))