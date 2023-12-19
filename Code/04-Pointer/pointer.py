from manimlib import *
import numpy as np

from manimlib.mobject.types.vectorized_mobject import VMobject

svg_path = "./images/svg/"


class OneColTable(VGroup):
    def __init__(
        self,
        labels=["0", "1", "2", "3", "4", "5", "6", "7"],
        label_color=WHITE,
        num_rows=8,
        width=1.2,
        height=0.8,
        text_scale=2,
        show_label=False,
        is_code=False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        assert len(labels) == num_rows

        self.rects = VGroup()
        self.labels = VGroup()

        for i in range(num_rows):
            rect = Rectangle(height=height, width=width)
            self.rects.add(rect)

            if show_label:
                if is_code:
                    label = Code(labels[i], font="Fira", language="c")
                else:
                    label = Text(labels[i], font_size=15, color=label_color)

                label.scale(text_scale).move_to(rect)
                self.labels.add(label)

        self.rects.arrange(DOWN, aligned_edge=LEFT, buff=0)

        if show_label:
            for i, label in enumerate(self.labels):
                label.next_to(self.rects[i], ORIGIN)
            self.add(self.rects, self.labels)
        else:
            self.add(self.rects)

    def get_row_rect(self, row_index) -> Rectangle:
        return self.rects[row_index]

    def get_row_label(self, row_index) -> MarkupText:
        return self.labels[row_index]


class MemoryModel(VGroup):
    def __init__(
        self,
        model_text: str,
        address_text: str,
        width=6,
        height=2,
        color=BLUE_D,
        color_opacity=0.4,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.rect = Rectangle(
            height=height, width=width, fill_color=color, fill_opacity=color_opacity
        )
        label_left = Text(model_text, color=WHITE).scale(1.4)
        label_right = Text(address_text, color=YELLOW_C).scale(1.2)
        self.label = VGroup(label_left, label_right)
        self.label.arrange(RIGHT, buff=0.2)
        self.label.next_to(self.rect, ORIGIN)
        self.add(self.rect, self.label)

    def get_rect(self) -> Rectangle:
        return self.rect

    def get_label(self) -> VGroup:
        return self.label


class MiddlewareModel(VGroup):
    def __init__(
        self,
        text: str,
        width=6,
        height=1,
        radius=0.5,
        color=GREEN_B,
        color_opacity=0.4,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.rect = RoundedRectangle(
            height=height,
            width=width,
            corner_radius=radius,
            fill_color=color,
            fill_opacity=color_opacity,
        )
        self.label = Text(text, color=WHITE).scale(1.5)
        self.label.next_to(self.rect, ORIGIN)
        self.add(self.rect, self.label)

    def get_rect(self) -> RoundedRectangle:
        return self.rect

    def get_label(self) -> Text:
        return self.label


class CompilerCircle(VGroup):
    def __init__(self):
        def unit(angle):
            return np.array([np.cos(angle), np.sin(angle), 0])

        super().__init__()
        nums = 68
        radius_in = 2.5
        radius_out = 2.6
        circle_in = Circle(radius=radius_in, stroke_color=GREEN_B, stroke_width=2)
        circle_out = Circle(radius=radius_out, stroke_color=GREEN_B, stroke_width=2)
        circle = VGroup(circle_in, circle_out)
        # for i in range(nums):
        #     angle = i * TAU / nums
        #     mark_i = Line(radius_in * unit(angle), radius_out * unit(angle)).set_color(
        #         GREEN_B
        #     )
        #     circle.add(mark_i)
        self.add(circle)


class LanguageModel(VGroup):
    def __init__(self, text: str, text_scale=1.2, color=PURPLE_A, **kwargs):
        super().__init__(**kwargs)
        self.ellipse = Ellipse(
            fill_color=color, stroke_color=WHITE, fill_opacity=0.4
        ).scale(1.6)
        self.label = Text(text, color=WHITE).scale(text_scale)
        self.add(self.ellipse, self.label)

    def get_ellipse(self) -> Ellipse:
        return self.ellipse

    def get_label(self) -> Text:
        return self.label


class TreeNode(VGroup):
    def __init__(self, key_value, **kwargs):
        super().__init__(**kwargs)
        self.key = Rectangle(height=0.6, width=2, color=RED_C)
        self.left = Rectangle(height=0.5, width=1, color=GREEN_C).shift(
            LEFT * 0.5 + DOWN * 0.6
        )
        self.right = Rectangle(height=0.5, width=1, color=BLUE_C).shift(
            RIGHT * 0.5 + DOWN * 0.6
        )
        self.key_value = Text(str(key_value)).scale(0.5).move_to(self.key)
        self.left_text = Text("left").scale(0.5).move_to(self.left)
        self.right_text = Text("right").scale(0.5).move_to(self.right)

        self.add(
            self.key,
            self.left,
            self.right,
            self.key_value,
            self.left_text,
            self.right_text,
        )


class TreeModel(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_node = TreeNode("10")

        self.left_node = TreeNode("2").shift(LEFT * 1.8 + DOWN * 2)
        self.right_node = TreeNode("16").shift(RIGHT * 1.8 + DOWN * 2)
        self.left_right_node = TreeNode("8").shift(LEFT * 1 + DOWN * 4.2)

        width = 3

        self.arrow_to_left = Arrow(
            start=self.root_node.left.get_bottom(),
            end=self.left_node.key.get_top(),
            stroke_width=width,
            buff=0.1,
        )
        self.arrow_to_right = Arrow(
            start=self.root_node.right.get_bottom(),
            end=self.right_node.key.get_top(),
            stroke_width=width,
            buff=0.1,
        )
        self.arrow_to_left_right = Arrow(
            start=self.left_node.right.get_bottom(),
            end=self.left_right_node.key.get_top(),
            stroke_width=width,
            buff=0.1,
        )
        self.node_group = VGroup(
            self.root_node,
            self.left_node,
            self.right_node,
            self.left_right_node,
        )
        self.arrow_group = VGroup(
            self.arrow_to_left,
            self.arrow_to_right,
            self.arrow_to_left_right,
        )
        self.add(
            self.node_group,
            self.arrow_group,
        )

    def get_node_group(self) -> VGroup:
        return self.node_group

    def get_arrow_group(self) -> VGroup:
        return self.arrow_group


class MemoryTableRow(VGroup):
    def __init__(
        self,
        code_text: str,
        name_label: str,
        address_labels: list,
        value_label: str,
        show_code=True,
        address_row0_color=WHITE,
        value_color=WHITE,
        name_scale=4,
        address_scale=2,
        value_scale=2,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.name_table = OneColTable(
            labels=[name_label],
            num_rows=1,
            height=0.5 * len(address_labels),
            width=2,
            text_scale=name_scale,
            show_label=True,
        )
        self.code = Code(
            code=code_text,
            font="Fira",
            language="c",
        ).scale(2)
        self.code.next_to(self.name_table, LEFT, buff=0.4)
        self.address_table = OneColTable(
            labels=address_labels,
            num_rows=len(address_labels),
            height=0.5,
            width=3,
            text_scale=address_scale,
            show_label=True,
        )
        self.address_table.get_row_label(0).set_color(address_row0_color)
        self.address_table.next_to(self.name_table, RIGHT, buff=0)
        self.value_table = OneColTable(
            labels=[value_label],
            num_rows=1,
            height=0.5 * len(address_labels),
            width=2,
            text_scale=value_scale,
            show_label=True,
        )
        self.value_table.get_row_label(0).set_color(value_color)
        self.value_table.next_to(self.address_table, RIGHT, buff=0)
        if show_code:
            self.add(self.code, self.name_table, self.address_table, self.value_table)
        else:
            self.add(self.name_table, self.address_table, self.value_table)

    def get_code(self) -> Code:
        return self.code

    def get_name_table(self) -> OneColTable:
        return self.name_table

    def get_address_table(self) -> OneColTable:
        return self.address_table

    def get_value_table(self) -> OneColTable:
        return self.value_table


class MemoryTableOnePointer(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value_row = MemoryTableRow(
            code_text="""
            int a = 2568;
            """,
            name_label="a",
            address_labels=[
                "0xffffffffecdc",
                "0xffffffffecdd",
                "0xffffffffecde",
                "0xffffffffecdf",
            ],
            value_label="2568",
            address_row0_color=GOLD,
            value_color=PURPLE_B,
            value_scale=4,
        )

        self.pointer_row = MemoryTableRow(
            code_text="""
            int *p = &a;
            """,
            name_label="p",
            address_labels=[
                "0xffffffffece0",
                "0xffffffffece1",
                "0xffffffffece2",
                "0xffffffffece3",
                "0xffffffffece4",
                "0xffffffffece5",
                "0xffffffffece6",
                "0xffffffffece7",
            ],
            value_label="0xffffffffecdc",
            address_row0_color=MAROON,
            value_color=GOLD,
        )
        self.pointer_row.next_to(self.value_row, DOWN, buff=0).align_to(
            self.value_row, RIGHT
        )
        self.name_text = Text("变量", color=WHITE).scale(0.8)
        self.name_text.next_to(self.value_row.get_name_table(), UP, buff=0.2)
        self.address_text = Text("地址", color=WHITE).scale(0.8)
        self.address_text.next_to(self.value_row.get_address_table(), UP, buff=0.2)
        self.value_text = Text("值", color=WHITE).scale(0.8)
        self.text_group = VGroup(self.name_text, self.address_text, self.value_text)
        self.value_text.next_to(self.value_row.get_value_table(), UP, buff=0.2)

        self.add(
            self.text_group,
            self.value_row,
            self.pointer_row,
        )

    def get_value_row(self) -> MemoryTableRow:
        return self.value_row

    def get_pointer_row(self) -> MemoryTableRow:
        return self.pointer_row

    def get_text_group(self) -> VGroup:
        return self.text_group

    def get_pointer_value_label(self) -> MarkupText:
        return self.pointer_row.get_value_table().get_row_label(0)

    def get_value_address0_label(self) -> MarkupText:
        return self.value_row.get_address_table().get_row_label(0)


class MemoryTableTwoPointer(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.memory_table = MemoryTableOnePointer()
        self.pointer2_row = MemoryTableRow(
            code_text="""
            int **pp = &p;
            """,
            name_label="pp",
            address_labels=[
                "0xffffffffece8",
                "0xffffffffece9",
                "0xffffffffecea",
                "0xffffffffeceb",
                "0xffffffffecec",
                "0xffffffffeced",
                "0xffffffffecee",
                "0xffffffffecef",
            ],
            value_label="0xffffffffece0",
            address_row0_color=LIGHT_PINK,
            value_color=MAROON,
        )
        self.pointer2_row.next_to(self.memory_table, DOWN, buff=0).align_to(
            self.memory_table, RIGHT
        )
        self.add(self.memory_table, self.pointer2_row)

    def get_memory_table(self) -> MemoryTableOnePointer:
        return self.memory_table

    def get_pointer2_row(self) -> MemoryTableRow:
        return self.pointer2_row

    def get_pointer1_value_label(self) -> MarkupText:
        return self.memory_table.get_pointer_value_label()

    def get_value_address0_label(self) -> MarkupText:
        return self.memory_table.get_value_address0_label()

    def get_pointer2_value_label(self) -> MarkupText:
        return self.pointer2_row.get_value_table().get_row_label(0)

    def get_pointer1_address0_label(self) -> MarkupText:
        return self.memory_table.get_pointer_row().get_address_table().get_row_label(0)


class MemoryTableIntArr(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pointer_row = MemoryTableRow(
            code_text="""
            int *p = a;
            """,
            name_label="p",
            address_labels=[
                "0xffffffffecc0",
                "0xffffffffecc1",
                "0xffffffffecc2",
                "0xffffffffecc3",
                "0xffffffffecc4",
                "0xffffffffecc5",
                "0xffffffffecc6",
                "0xffffffffecc7",
            ],
            value_label="0xffffffffecc8",
            address_row0_color=MAROON,
            value_color=GOLD,
        )
        self.a0_table_row = MemoryTableRow(
            code_text="""
            int a[2] = {25, 68};
            """,
            name_label="a[0]",
            address_labels=[
                "0xffffffffecc8",
                "0xffffffffecc9",
                "0xffffffffecca",
                "0xffffffffeccb",
            ],
            value_label="25",
            address_row0_color=GOLD,
            value_color=PURPLE_B,
            value_scale=4,
            show_code=False,
        )
        self.a0_table_row.next_to(self.pointer_row, DOWN, buff=0).align_to(
            self.pointer_row, RIGHT
        )
        self.a1_table_row = MemoryTableRow(
            code_text="""
            int a[2] = {25, 68};
            """,
            name_label="a[1]",
            address_labels=[
                "0xffffffffeccc",
                "0xffffffffeccd",
                "0xffffffffecce",
                "0xffffffffeccf",
            ],
            value_label="68",
            address_row0_color=GREEN_C,
            value_color=PURPLE_B,
            value_scale=4,
            show_code=False,
        )
        self.a1_table_row.next_to(self.a0_table_row, DOWN, buff=0).align_to(
            self.a0_table_row, RIGHT
        )
        self.arr_code = Code(
            code="""
            int a[2] 
            = {25, 68};
            """,
            font="Fira",
            language="c",
        ).scale(2)
        self.arr_code.next_to(self.a1_table_row, LEFT, buff=0.2).shift(UP)

        self.name_text = Text("变量", color=WHITE).scale(0.8)
        self.name_text.next_to(self.pointer_row.get_name_table(), UP, buff=0.2)
        self.address_text = Text("地址", color=WHITE).scale(0.8)
        self.address_text.next_to(self.pointer_row.get_address_table(), UP, buff=0.2)
        self.value_text = Text("值", color=WHITE).scale(0.8)
        self.value_text.next_to(self.pointer_row.get_value_table(), UP, buff=0.2)
        self.text_group = VGroup(self.name_text, self.address_text, self.value_text)

        self.add(
            self.text_group,
            self.arr_code,
            self.pointer_row,
            self.a0_table_row,
            self.a1_table_row,
        )

    def get_pointer_row(self) -> MemoryTableRow:
        return self.pointer_row

    def get_a0_row(self) -> MemoryTableRow:
        return self.a0_table_row

    def get_a1_row(self) -> MemoryTableRow:
        return self.a1_table_row

    def get_pointer_value_label(self) -> MarkupText:
        return self.pointer_row.get_value_table().get_row_label(0)

    def get_a0_address0_label(self) -> MarkupText:
        return self.a0_table_row.get_address_table().get_row_label(0)

    def get_a1_address0_label(self) -> MarkupText:
        return self.a1_table_row.get_address_table().get_row_label(0)


class MemoryTableDoubleArr(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pointer_row = MemoryTableRow(
            code_text="""
            double *p = d;
            """,
            name_label="p",
            address_labels=[
                "0xffffffffecc0",
                "0xffffffffecc1",
                "0xffffffffecc2",
                "0xffffffffecc3",
                "0xffffffffecc4",
                "0xffffffffecc5",
                "0xffffffffecc6",
                "0xffffffffecc7",
            ],
            value_label="0xffffffffecc8",
            address_row0_color=MAROON,
            value_color=GOLD,
        )
        self.d0_table_row = MemoryTableRow(
            code_text="""
            double d[2] = {25.0, 68.0};
            """,
            name_label="d[0]",
            address_labels=[
                "0xffffffffecc8",
                "0xffffffffecc9",
                "0xffffffffecca",
                "0xffffffffeccb",
                "0xffffffffeccc",
                "0xffffffffeccd",
                "0xffffffffecce",
                "0xffffffffeccf",
            ],
            value_label="25.0",
            address_row0_color=GOLD,
            value_color=PURPLE_B,
            value_scale=4,
            show_code=False,
        )
        self.d0_table_row.next_to(self.pointer_row, DOWN, buff=0).align_to(
            self.pointer_row, RIGHT
        )
        self.d1_table_row = MemoryTableRow(
            code_text="""
            double d[2] = {25.0, 68.0};
            """,
            name_label="d[1]",
            address_labels=[
                "0xffffffffecd0",
                "0xffffffffecd1",
                "0xffffffffecd2",
                "0xffffffffecd3",
                "0xffffffffecd4",
                "0xffffffffecd5",
                "0xffffffffecd6",
                "0xffffffffecd7",
            ],
            value_label="68.0",
            address_row0_color=GREEN_C,
            value_color=PURPLE_B,
            value_scale=4,
            show_code=False,
        )
        self.d1_table_row.next_to(self.d0_table_row, DOWN, buff=0).align_to(
            self.d0_table_row, RIGHT
        )
        self.arr_code = Code(
            code="""
            double d[2] 
            = {25.0, 68.0};
            """,
            font="Fira",
            language="c",
        ).scale(2)
        self.arr_code.next_to(self.d1_table_row, LEFT, buff=0.2).shift(UP * 2)

        self.name_text = Text("变量", color=WHITE).scale(0.8)
        self.name_text.next_to(self.pointer_row.get_name_table(), UP, buff=0.2)
        self.address_text = Text("地址", color=WHITE).scale(0.8)
        self.address_text.next_to(self.pointer_row.get_address_table(), UP, buff=0.2)
        self.value_text = Text("值", color=WHITE).scale(0.8)
        self.value_text.next_to(self.pointer_row.get_value_table(), UP, buff=0.2)
        self.text_group = VGroup(self.name_text, self.address_text, self.value_text)

        self.add(
            self.text_group,
            self.pointer_row,
            self.d0_table_row,
            self.d1_table_row,
            self.arr_code,
        )

    def get_pointer_row(self) -> MemoryTableRow:
        return self.pointer_row

    def get_d0_table_row(self) -> MemoryTableRow:
        return self.d0_table_row

    def get_d1_table_row(self) -> MemoryTableRow:
        return self.d1_table_row

    def get_pointer_value_label(self) -> MarkupText:
        return self.pointer_row.get_value_table().get_row_label(0)

    def get_d0_address0_label(self) -> MarkupText:
        return self.d0_table_row.get_address_table().get_row_label(0)

    def get_d1_address0_label(self) -> MarkupText:
        return self.d1_table_row.get_address_table().get_row_label(0)


class MemoryTableReference(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value_row = MemoryTableRow(
            code_text="""
            int a = 2568;
            """,
            name_label="a",
            address_labels=[
                "0xffffffffecdc",
                "0xffffffffecdd",
                "0xffffffffecde",
                "0xffffffffecdf",
            ],
            value_label="2568",
            address_row0_color=GOLD,
            value_color=PURPLE_B,
            value_scale=4,
        )
        self.value_row.get_name_table().get_row_label(0).set_color(GREEN)

        self.reference_row = MemoryTableRow(
            code_text="""
            int &ref = a;
            """,
            name_label="ref",
            address_labels=[
                "0xffffffffece0",
                "0xffffffffece1",
                "0xffffffffece2",
                "0xffffffffece3",
                "0xffffffffece4",
                "0xffffffffece5",
                "0xffffffffece6",
                "0xffffffffece7",
            ],
            value_label="0xffffffffecdc",
            address_row0_color=MAROON,
            value_color=GOLD,
        )
        self.reference_row.get_name_table().get_row_label(0).set_color(GREEN)
        self.reference_row.next_to(self.value_row, DOWN, buff=0).align_to(
            self.value_row, RIGHT
        )
        self.name_text = Text("变量", color=WHITE).scale(0.8)
        self.name_text.next_to(self.value_row.get_name_table(), UP, buff=0.2)
        self.address_text = Text("地址", color=WHITE).scale(0.8)
        self.address_text.next_to(self.value_row.get_address_table(), UP, buff=0.2)
        self.value_text = Text("值", color=WHITE).scale(0.8)
        self.text_group = VGroup(self.name_text, self.address_text, self.value_text)
        self.value_text.next_to(self.value_row.get_value_table(), UP, buff=0.2)

        self.add(
            self.text_group,
            self.value_row,
            self.reference_row,
        )

    def get_value_row(self) -> MemoryTableRow:
        return self.value_row

    def get_reference_row(self) -> MemoryTableRow:
        return self.reference_row

    def get_text_group(self) -> VGroup:
        return self.text_group

    def get_value_name_label(self) -> MarkupText:
        return self.value_row.get_name_table().get_row_label(0)

    def get_reference_name_label(self) -> MarkupText:
        return self.reference_row.get_name_table().get_row_label(0)


######################################################################################################


class Intro(Scene):
    def construct(self) -> None:
        saying = Text(
            """
                      我语言的极限，便是我世界的极限
                      """,
            color=WHITE,
            t2c={"语言": BLUE_B, "世界": YELLOW_B},
        ).move_to(ORIGIN)
        saying_author = (
            Text(
                """
                 《逻辑哲学论》5.6 1918
                 —— Ludwig Wittgenstein
                 """,
                color=YELLOW,
            )
            .scale(0.8)
            .next_to(saying, DOWN, buff=0.4)
            .shift(RIGHT * 4)
        )

        self.play(Write(saying), run_time=2)
        self.wait()
        self.play(Write(saying_author))
        self.wait(2)
        self.play(FadeOut(saying), FadeOut(saying_author))
        self.wait()

        point_title = Text("指针(Pointer)", color=WHITE).scale(1.5)

        line = Line(LEFT * 5.5, RIGHT * 5.5, color=WHITE)

        titan_c = ImageMobject("titan_c.png").scale(1.3)

        beginner_concepts = [
            "指针操作",
            "指针数组",
            "数组指针",
        ]

        advanced_concepts = [
            "野指针",
            "多级指针",
            "内存泄漏",
        ]

        beginner_texts = VGroup(
            *[Text(concept).scale(0.8) for concept in beginner_concepts]
        )
        advanced_texts = VGroup(
            *[Text(concept).scale(0.8) for concept in advanced_concepts]
        )

        beginner_texts.arrange(DOWN, aligned_edge=ORIGIN)
        advanced_texts.arrange(DOWN, aligned_edge=ORIGIN)

        beginner_texts.next_to(titan_c, LEFT, buff=1)
        advanced_texts.next_to(titan_c, RIGHT, buff=1)

        self.play(Write(point_title))
        self.wait()

        point_title.generate_target()
        point_title.target.to_edge(UP).scale(0.8)
        line.next_to(point_title.target, DOWN)
        titan_c.next_to(line, DOWN)

        self.play(MoveToTarget(point_title))
        self.play(GrowFromCenter(line))
        self.wait()
        self.play(FadeIn(titan_c))
        self.wait()
        self.play(Write(beginner_texts))
        self.wait()
        self.play(Write(advanced_texts))
        self.wait(3)
        for i in range(len(beginner_texts)):
            self.play(
                beginner_texts[i]
                .animate.shift(LEFT * 5 + random.uniform(-3, 3) * UP)
                .set_opacity(0),
                run_time=0.5,
                rate_func=linear,
            )

        for text in advanced_texts:
            self.play(
                text.animate.shift(
                    RIGHT * 5 + random.uniform(-3, 3) * DOWN
                ).set_opacity(0),
                run_time=0.5,
                rate_func=linear,
            )
        self.play(FadeOut(titan_c), FadeOut(line), FadeOut(point_title))
        self.wait()

        self.clear()


class PointerExplain(Scene):
    def construct(self) -> None:
        title = Text(
            "指针: 一种保存变量地址的变量 ——《C程序设计语言》", color=WHITE, t2c={"地址": GOLD}
        ).scale(1)
        title.to_edge(UL)
        self.play(Write(title))
        self.wait()

        mem = MemoryTableOnePointer().scale(0.8).move_to(ORIGIN)
        mem_text_group = mem.get_text_group()
        mem_value_row = mem.get_value_row()
        mem_pointer_row = mem.get_pointer_row()
        self.play(Write(mem_text_group))
        self.wait()
        self.play(ShowCreation(mem_value_row), run_time=2)
        self.wait()
        self.play(ShowCreation(mem_pointer_row), run_time=2)
        self.wait()

        # 0xffffffffecdc变为0xdc, 0xec, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00上下排列
        pointer_value_split_text = Text(
            """
        0xdc
        0xec
        0xff
        0xff
        0xff
        0xff
        0x00
        0x00
        """,
            color=GOLD,
        ).scale(0.7)
        pointer_value_split_text.next_to(mem.get_pointer_value_label(), ORIGIN)
        pointer_value_label = mem.get_pointer_value_label().copy()
        self.play(
            ReplacementTransform(
                mem.get_pointer_value_label(), pointer_value_split_text
            )
        )
        self.wait()
        self.play(ReplacementTransform(pointer_value_split_text, pointer_value_label))
        self.wait()

        arrow = CurvedArrow(
            start_point=pointer_value_label.get_right() + RIGHT * 0.15,
            end_point=mem.get_value_address0_label().get_right(),
            stroke_width=4,
            angle=TAU / 3,
        ).set_color(GOLD)
        self.play(GrowArrow(arrow))
        self.wait()

        self.play(Indicate(mem_value_row.get_code()[0:3], scale_factor=2))
        self.wait()
        self.play(FlashAround(mem_value_row.get_address_table()))
        self.play(Indicate(mem_pointer_row.get_code()[0:3], scale_factor=2))
        self.wait()
        self.play(FlashAround(mem_pointer_row.get_address_table()))
        self.wait()

        self.clear()


class TypeExplain(Scene):
    def construct(self) -> None:
        mem_int_arr = MemoryTableIntArr().scale(0.8).move_to(ORIGIN)

        arrow0_mem_int_arr = CurvedArrow(
            start_point=mem_int_arr.get_pointer_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_int_arr.get_a0_address0_label().get_right(),
            stroke_width=4,
            angle=-TAU / 4,
        ).set_color(GOLD)

        arrow1_mem_int_arr = CurvedArrow(
            start_point=mem_int_arr.get_pointer_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_int_arr.get_a1_address0_label().get_right(),
            stroke_width=4,
            angle=-TAU / 4,
        ).set_color(GREEN_C)

        arrow0_int_text = Text("P", color=GOLD).scale(1.28)
        arrow0_int_text.next_to(arrow0_mem_int_arr, ORIGIN, buff=0.16)
        arrow1_int_text = Text("P+1", color=GREEN_C).scale(1.28)
        arrow1_int_text.next_to(arrow1_mem_int_arr, RIGHT, buff=0.15)
        arrow1_int_text1 = Text(
            "0xffffffffecc8 + 0x4", t2c={"0x4": BLUE, "0xffffffffecc8": GOLD}
        ).scale(0.64)
        arrow1_int_text1.next_to(arrow1_int_text, DOWN, buff=0.8)
        arrow1_int_text2text1_arrow = Arrow(
            start=arrow1_int_text.get_bottom() + UP * 0.05,
            end=arrow1_int_text1.get_top() + DOWN * 0.05,
            stroke_width=3.2,
        )
        mem_int_arr_group = VGroup(
            mem_int_arr,
            arrow0_mem_int_arr,
            arrow1_mem_int_arr,
            arrow0_int_text,
            arrow1_int_text,
            arrow1_int_text1,
            arrow1_int_text2text1_arrow,
        )

        self.play(ShowCreation(mem_int_arr))
        self.wait()
        self.play(GrowArrow(arrow0_mem_int_arr))
        self.wait()
        self.play(Write(arrow0_int_text))
        self.wait()
        self.play(GrowArrow(arrow1_mem_int_arr))
        self.wait()
        self.play(Write(arrow1_int_text))
        self.wait()
        self.play(GrowArrow(arrow1_int_text2text1_arrow))
        self.wait()
        self.play(Write(arrow1_int_text1))
        self.wait()

        mem_int_arr_group.generate_target()
        mem_int_arr_group.target.scale(0.625).to_edge(UL).shift(RIGHT * 0.2)
        divide_line = Line(UP * 3.5, DOWN * 3, color=WHITE)
        self.play(MoveToTarget(mem_int_arr_group))
        self.wait()
        self.play(GrowFromCenter(divide_line))
        self.wait()

        mem_double_arr = MemoryTableDoubleArr().scale(0.5).to_edge(UR).shift(LEFT * 1.2)
        arrow0_mem_double_arr = CurvedArrow(
            start_point=mem_double_arr.get_pointer_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_double_arr.get_d0_address0_label().get_right(),
            stroke_width=4,
            angle=-TAU / 4,
        ).set_color(GOLD)

        arrow1_mem_double_arr = CurvedArrow(
            start_point=mem_double_arr.get_pointer_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_double_arr.get_d1_address0_label().get_right(),
            stroke_width=4,
            angle=-TAU / 4,
        ).set_color(GREEN_C)

        arrow0_double_text = Text("P", color=GOLD).scale(0.8)
        arrow0_double_text.next_to(arrow0_mem_double_arr, ORIGIN, buff=0.1)
        arrow1_double_text = Text("P+1", color=GREEN_C).scale(0.8)
        arrow1_double_text.next_to(arrow1_mem_double_arr, RIGHT, buff=0.15)
        arrow1_double_text1 = Text(
            "0xffffffffecc8 + 0x8", t2c={"0x8": BLUE, "0xffffffffecc8": GOLD}
        ).scale(0.4)
        arrow1_double_text1.next_to(arrow1_double_text, DOWN, buff=0.65)
        arrow1_double_text2text1_arrow = Arrow(
            start=arrow1_double_text.get_bottom() + UP * 0.06,
            end=arrow1_double_text1.get_top() + DOWN * 0.06,
            stroke_width=3.2,
        )
        self.play(ShowCreation(mem_double_arr))
        self.wait()
        self.play(GrowArrow(arrow0_mem_double_arr))
        self.wait()
        self.play(Write(arrow0_double_text))
        self.wait()
        self.play(GrowArrow(arrow1_mem_double_arr))
        self.wait()
        self.play(Write(arrow1_double_text))
        self.wait()
        self.play(GrowArrow(arrow1_double_text2text1_arrow))
        self.wait()
        self.play(Write(arrow1_double_text1))
        self.wait()

        title1 = Text("指针大小与指针类型无关").scale(1)
        title1.to_edge(DL).shift(UP * 1.5 + RIGHT * 0.3)
        title2 = Text("指针类型决定地址偏移量", color=BLUE).scale(1.2)
        title2.next_to(title1, DOWN, buff=0.2)
        self.play(Write(title1))
        self.wait()
        self.play(Write(title2))
        self.wait()

        self.clear()


class PointerAbstract(Scene):
    def construct(self) -> None:
        mem_one_pointer = MemoryTableOnePointer().scale(0.8).move_to(ORIGIN)
        mem_one_pointer_arrow = CurvedArrow(
            start_point=mem_one_pointer.get_pointer_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_one_pointer.get_value_address0_label().get_right(),
            stroke_width=4,
            angle=TAU / 3,
        ).set_color(GOLD)
        mem_one_pointer_group = VGroup(mem_one_pointer, mem_one_pointer_arrow)

        self.play(FadeIn(mem_one_pointer_group))
        self.wait()
        mem_one_pointer_group.generate_target()
        mem_one_pointer_group.target.scale(0.8).to_edge(UL).shift(
            RIGHT * 0.2 + DOWN * 1.5
        )
        self.play(MoveToTarget(mem_one_pointer_group))
        self.wait()

        mem_two_pointer = (
            MemoryTableTwoPointer()
            .scale(0.6)
            .to_edge(UR)
            .shift(LEFT * 0.1 + DOWN * 0.3)
        )
        mem_two_pointer_mem_table = mem_two_pointer.get_memory_table()
        mem_two_pointer_pointer2_row = mem_two_pointer.get_pointer2_row()
        mem_two_pointer_arrow1 = CurvedArrow(
            start_point=mem_two_pointer.get_pointer1_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_two_pointer.get_value_address0_label().get_right(),
            stroke_width=4,
            angle=TAU / 3,
        ).set_color(GOLD)
        mem_two_pointer_arrow2 = CurvedArrow(
            start_point=mem_two_pointer.get_pointer2_value_label().get_right()
            + RIGHT * 0.15,
            end_point=mem_two_pointer.get_pointer1_address0_label().get_right(),
            stroke_width=4,
            angle=TAU / 3,
        ).set_color(MAROON)

        mem_one_pointer_copy = mem_one_pointer.copy()
        self.play(ReplacementTransform(mem_one_pointer_copy, mem_two_pointer_mem_table))
        self.wait()
        self.play(ShowCreation(mem_two_pointer_pointer2_row), run_time=2)
        self.wait()
        self.play(GrowArrow(mem_two_pointer_arrow2))
        self.wait()
        self.play(GrowArrow(mem_two_pointer_arrow1))
        self.wait()

        mem_two_pointer_group = VGroup(
            mem_two_pointer,
            mem_two_pointer_arrow1,
            mem_two_pointer_arrow2,
        )
        mem_one_pointer_group.generate_target()
        mem_one_pointer_group.target.scale(0.6).shift(DOWN * 1.6)
        mem_two_pointer_group.generate_target()
        mem_two_pointer_group.target.scale(0.55).shift(DOWN * 1.9 + LEFT * 1)
        self.play(
            MoveToTarget(mem_two_pointer_group), MoveToTarget(mem_one_pointer_group)
        )
        self.wait()

        level1_title = Text("指针是保存变量地址的变量", color=BLUE).scale(0.8)
        level1_title.next_to(mem_one_pointer_group, DOWN, buff=0.2)
        mem_one_pointer_group.add(level1_title)
        self.play(Write(level1_title))
        self.wait()

        divided_line1 = Line(LEFT * 5.5, RIGHT * 5, color=WHITE, stroke_width=2)
        self.play(GrowFromCenter(divided_line1))
        self.wait()

        memory_rect1 = OneColTable(width=1.8).scale(0.5).to_edge(UL).shift(RIGHT * 4)

        address_text = Text("0xffffffffecdc", color=YELLOW_B).scale(0.6)
        address_text.next_to(memory_rect1.get_row_rect(0), LEFT).shift(LEFT * 1)

        pointer1_rect = Rectangle(height=0.5, width=2, color=GOLD)
        pointer1_rect.next_to(memory_rect1.get_row_rect(0), LEFT).shift(LEFT * 0.8)
        pointer1_dot = (
            Dot().set_color(GOLD).scale(0.7).move_to(pointer1_rect.get_center())
        )
        pointer1 = Arrow(
            pointer1_dot.get_center() + LEFT * 0.22,
            memory_rect1.get_row_rect(0).get_left() + RIGHT * 0.2,
            stroke_color=GOLD,
            stroke_width=4,
        )
        pointer1_text = Text("P", color=GOLD).scale(0.8)
        pointer1_text.next_to(pointer1_rect, DOWN, buff=0.1)
        level2_title = Text("指针是地址?", color=BLUE).scale(0.8)
        level2_title.next_to(pointer1_text, DOWN, buff=0.1).shift(DOWN)

        self.play(FadeIn(memory_rect1))
        self.wait()
        self.play(Write(address_text))
        self.wait()
        self.play(ShowCreation(pointer1_rect))
        self.wait()
        self.play(ReplacementTransform(address_text, pointer1_text))
        self.wait()
        self.play(FadeIn(pointer1_dot), GrowArrow(pointer1))
        self.wait()
        self.play(Write(level2_title))
        self.wait()

        memory_group1 = VGroup(
            memory_rect1,
            pointer1_rect,
            pointer1_dot,
            pointer1,
            pointer1_text,
        )

        memory_rect2 = memory_group1.copy().to_edge(UR).shift(LEFT * 2.5)
        address_text2 = Text("0xffffffffece0", color=MAROON).scale(0.6)
        address_text2.next_to(memory_rect2[1], DOWN).shift(DOWN * 1)
        pointer2_rect = Rectangle(height=0.5, width=2, color=MAROON)
        pointer2_rect.next_to(memory_rect2[1], DOWN).shift(DOWN * 0.8)
        pointer2_dot = (
            Dot().set_color(MAROON).scale(0.7).move_to(pointer2_rect.get_center())
        )
        pointer2 = Arrow(
            pointer2_dot.get_center() + DOWN * 0.3,
            memory_rect2[1].get_bottom() + DOWN * 0.15,
            stroke_color=MAROON,
            stroke_width=4,
        )
        pointer2_text = Text("PP", color=MAROON).scale(0.8)
        pointer2_text.next_to(pointer2_rect, DOWN, buff=0.1)

        self.play(FadeIn(memory_rect2))
        self.wait()
        self.play(Write(address_text2))
        self.wait()
        self.play(ShowCreation(pointer2_rect))
        self.wait()
        self.play(ReplacementTransform(address_text2, pointer2_text))
        self.wait()
        self.play(FadeIn(pointer2_dot), GrowArrow(pointer2))
        self.wait()

        level2_group = VGroup(
            memory_rect2,
            pointer2_rect,
            pointer2_dot,
            pointer2,
            pointer2_text,
            memory_group1,
            divided_line1,
            mem_one_pointer_group,
            mem_two_pointer_group,
            level2_title,
        )
        # level2_group.generate_target()
        # level2_group.target.scale(0.82).to_edge(LEFT).shift(RIGHT * 0.08)
        # self.play(MoveToTarget(level2_group))
        # self.wait()

        # divided_line2 = Line(UP * 3.5, DOWN * 3.5, color=WHITE, stroke_width=2).shift(
        #     RIGHT * 2.4
        # )
        # self.play(GrowFromCenter(divided_line2))
        # self.wait()

        # tree_model = TreeModel().scale(0.7).to_edge(UR).shift(DOWN * 1.5)
        # tree_model_node_group = tree_model.get_node_group()
        # tree_model_arrow_group = tree_model.get_arrow_group()
        # level3_title = Text("不再关注地址细节", color=BLUE).scale(0.8)
        # level3_title.next_to(tree_model, UP, buff=0.1).shift(UP * 0.3)
        # self.play(ShowCreation(tree_model_node_group))
        # self.wait()
        # for arrow in tree_model_arrow_group:
        #     self.play(GrowArrow(arrow))
        # self.wait()
        # self.play(Write(level3_title))
        # self.wait()

        # self.clear()


class AddressAbstract(Scene):
    def construct(self) -> None:
        physical_memory = MemoryModel("物理内存", ": 物理地址")
        physical_memory_rect = physical_memory.get_rect()
        physical_memory_label = physical_memory.get_label()

        self.play(FadeIn(physical_memory_rect))
        self.wait()
        self.play(Write(physical_memory_label))
        self.wait()
        physical_memory.generate_target()
        physical_memory.target.to_edge(DOWN).scale(0.6)
        self.play(MoveToTarget(physical_memory))
        self.wait()

        physical_memory2operation_system_arrow = Arrow(
            physical_memory_rect.get_corner(UP) + DOWN * 0.12,
            physical_memory_rect.get_corner(UP) + UP * 1.5,
            stroke_width=3,
        )

        operation_system = MiddlewareModel("操作系统").scale(0.8)
        operation_system_rect = operation_system.get_rect()
        operation_system_label = operation_system.get_label()
        operation_system.next_to(physical_memory2operation_system_arrow, UP, buff=0.12)

        os2left_virtual_memory_arrow = Arrow(
            operation_system_rect.get_corner(UP) + DOWN * 0 + LEFT * 1,
            operation_system_rect.get_corner(UP) + UP * 1.5 + LEFT * 3,
            stroke_width=3,
        )

        os2right_virtual_memory_arrow = Arrow(
            operation_system_rect.get_corner(UP) + DOWN * 0 + RIGHT * 1,
            operation_system_rect.get_corner(UP) + UP * 1.5 + RIGHT * 3,
            stroke_width=3,
        )

        left_virtual_memory = MemoryModel("虚拟内存", ": 虚拟地址", width=8).scale(0.6)
        left_virtual_memory_rect = left_virtual_memory.get_rect()
        left_virtual_memory_label = left_virtual_memory.get_label()
        left_virtual_memory.next_to(os2left_virtual_memory_arrow, UP, buff=0.12).shift(
            LEFT * 0.9
        )

        right_virtual_memory = MemoryModel("虚拟内存", ": 虚拟地址", width=8).scale(0.6)
        right_virtual_memory_rect = right_virtual_memory.get_rect()
        right_virtual_memory_label = right_virtual_memory.get_label()
        right_virtual_memory.next_to(
            os2right_virtual_memory_arrow, UP, buff=0.12
        ).shift(RIGHT * 0.9)

        self.play(GrowArrow(physical_memory2operation_system_arrow))
        self.wait()
        self.play(FadeIn(operation_system_rect))
        self.wait()
        self.play(Write(operation_system_label))
        self.wait()
        self.play(
            GrowArrow(os2left_virtual_memory_arrow),
            GrowArrow(os2right_virtual_memory_arrow),
        )
        self.wait()
        self.play(FadeIn(left_virtual_memory_rect), FadeIn(right_virtual_memory_rect))
        self.wait()
        self.play(Write(left_virtual_memory_label), Write(right_virtual_memory_label))
        self.wait()

        virtual_os_physical_group = VGroup(
            operation_system,
            physical_memory,
            left_virtual_memory,
            right_virtual_memory,
            os2left_virtual_memory_arrow,
            os2right_virtual_memory_arrow,
            physical_memory2operation_system_arrow,
        )
        virtual_os_physical_group.generate_target()
        virtual_os_physical_group.target.scale(0.55).to_edge(DOWN)
        self.play(MoveToTarget(virtual_os_physical_group))

        compiler = MiddlewareModel(
            "编\n译\n器",
            width=1,
            height=7,
        ).scale(0.5)
        compiler_rect = compiler.get_rect()
        compiler_label = compiler.get_label()

        compiler.next_to(left_virtual_memory_rect, LEFT, buff=0.4).shift(UP * 2.2)
        self.play(FadeIn(compiler_rect))
        self.wait()
        self.play(Write(compiler_label))
        self.wait()

        left_virtual_memory2assembly_arrow = Arrow(
            left_virtual_memory_rect.get_corner(UP) + DOWN * 0.12,
            left_virtual_memory_rect.get_corner(UP) + UP * 1,
            stroke_color=ORANGE,
            stroke_width=4,
        )

        compiler2assembly_arrow = Arrow(
            compiler_rect.get_corner(DR) + UP * 0.35,
            compiler_rect.get_corner(DR) + UP * 0.35 + RIGHT * 1.6,
            stroke_color=RED_A,
            stroke_width=8,
        )

        assembly_language = LanguageModel("汇编: 直接操作", text_scale=0.9).scale(0.5)
        assembly_language_ellipse = assembly_language.get_ellipse()
        assembly_language_label = assembly_language.get_label()
        assembly_language.next_to(left_virtual_memory2assembly_arrow, UP, buff=0.12)

        self.play(GrowArrow(compiler2assembly_arrow))
        self.wait()
        self.play(GrowArrow(left_virtual_memory2assembly_arrow))
        self.wait()
        self.play(FadeIn(assembly_language_ellipse))
        self.wait()
        self.play(Write(assembly_language_label))
        self.wait()

        fade_out_group = VGroup(
            operation_system,
            physical_memory,
            right_virtual_memory,
            os2left_virtual_memory_arrow,
            os2right_virtual_memory_arrow,
            physical_memory2operation_system_arrow,
        )
        assembly_compiler_group = VGroup(
            compiler,
            left_virtual_memory,
            assembly_language,
            compiler2assembly_arrow,
            left_virtual_memory2assembly_arrow,
        )
        self.play(FadeOut(fade_out_group))
        self.wait()
        assembly_compiler_group.generate_target()
        assembly_compiler_group.target.scale(1.5).shift(DOWN + LEFT * 0.8)
        self.play(MoveToTarget(assembly_compiler_group))
        self.wait()

        assembly_code_arm_str = """
        mov	w0, 2568
        str	w0, [sp, 28]

        add	x0, sp, 28
        str	x0, [sp, 32]
        """
        assembly_code_arm = (
            Code(
                code=assembly_code_arm_str,
                font="Fira",
                language="asm",
            )
            .scale(2)
            .next_to(assembly_compiler_group, RIGHT, buff=0.5)
            .shift(DOWN * 0.8 + RIGHT * 0.9)
        )
        assembly_code_arm_rect = SurroundingRectangle(
            assembly_code_arm, color=YELLOW, stroke_width=2, buff=0.3
        )
        assembly_code_arm_group = VGroup(assembly_code_arm_rect, assembly_code_arm)

        instructions_text = Text("指令", color=GREEN_B).scale(0.8)
        instructions_text.next_to(assembly_code_arm_rect, UL, buff=0.2).shift(
            RIGHT * 1.2
        )
        registers_text = Text("寄存器", color=BLUE).scale(0.8)
        registers_text.next_to(instructions_text, RIGHT, buff=0.1)
        immediate_text = Text("立即数", color=PURPLE_A).scale(0.8)
        immediate_text.next_to(registers_text, RIGHT, buff=0.3)

        memory_operate_rect = SurroundingRectangle(
            assembly_code_arm[17:22], color=RED, stroke_width=5, buff=0.2
        )

        memory_operate_arrow = Arrow(
            memory_operate_rect.get_corner(RIGHT) + LEFT * 0.1,
            memory_operate_rect.get_corner(RIGHT) + RIGHT * 0.8,
            stroke_color=RED,
            stroke_width=3,
        )

        memory_operate_text = Text("内存操作", color=RED).scale(0.8)
        memory_operate_text.next_to(memory_operate_arrow, RIGHT, buff=0.1)

        self.play(Write(assembly_code_arm))
        self.wait()
        self.play(ShowCreation(assembly_code_arm_rect))
        self.wait()
        self.play(Write(instructions_text))
        self.wait()
        self.play(Write(registers_text))
        self.wait()
        self.play(Write(immediate_text))
        self.wait()
        self.play(ShowCreation(memory_operate_rect))
        self.wait()
        self.play(GrowArrow(memory_operate_arrow))
        self.wait()
        self.play(Write(memory_operate_text))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    instructions_text,
                    registers_text,
                    immediate_text,
                    memory_operate_rect,
                    memory_operate_arrow,
                    memory_operate_text,
                )
            )
        )
        self.wait()

        assembly_code_arm_group.generate_target()
        assembly_code_arm_group.target.scale(0.7).shift(LEFT + DOWN * 0.5)
        self.play(MoveToTarget(assembly_code_arm_group))
        assembly_code_arm_text = Text("ARM 架构", color=YELLOW).scale(0.8)
        assembly_code_arm_text.next_to(assembly_code_arm_group, DOWN, buff=0.1)
        self.play(Write(assembly_code_arm_text))
        self.wait()

        assembly_code_riscv_str = """
        li	a5,2568
        sw	a5,-28(s0)

        addi a5,s0,-28
        sd	a5,-24(s0)"""
        assembly_code_riscv = (
            Code(
                code=assembly_code_riscv_str,
                font="Fira",
                language="asm",
            )
            .scale(2)
            .next_to(assembly_code_arm_group.target, RIGHT, buff=0.2)
        )
        assembly_code_riscv_rect = SurroundingRectangle(
            assembly_code_riscv, color=YELLOW, stroke_width=2, buff=0.3
        )
        assembly_code_riscv_group = VGroup(
            assembly_code_riscv_rect, assembly_code_riscv
        ).scale(0.7)
        assembly_code_riscv_text = Text("RISC-V 架构", color=YELLOW).scale(0.8)
        assembly_code_riscv_text.next_to(assembly_code_riscv_group, DOWN, buff=0.1)

        self.play(Write(assembly_code_riscv))
        self.wait()
        self.play(ShowCreation(assembly_code_riscv_rect))
        self.wait()
        self.play(Write(assembly_code_riscv_text))
        self.wait()

        c_code_str = """
        int a = 2568;
        int *p = &a;
        """
        c_code = (
            Code(
                code=c_code_str,
                font="Fira",
                language="c",
            )
            .scale(2)
            .next_to(assembly_code_riscv_group, UP, buff=0.2)
            .shift(LEFT * 1.6 + UP * 1.2)
        )
        c_code_rect = SurroundingRectangle(
            c_code, color=YELLOW, stroke_width=2, buff=0.3
        )
        c_code_group = VGroup(c_code_rect, c_code)
        c_code_text = Text("C", color=YELLOW).scale(0.8)
        c_code_text.next_to(c_code_group, DOWN, buff=0.1)

        self.play(Write(c_code))
        self.wait()
        self.play(ShowCreation(c_code_rect))
        self.wait()
        self.play(Write(c_code_text))
        self.wait()

        assembly2c_arrow = Arrow(
            assembly_language.get_corner(UP) + DOWN * 0.1,
            assembly_language.get_corner(UP) + UP * 1.35,
            stroke_color=ORANGE,
            stroke_width=4,
        )
        compiler2c_arrow = Arrow(
            compiler_rect.get_corner(UR) + DOWN * 2.3 + RIGHT * 0.1,
            compiler_rect.get_corner(UR) + DOWN * 2.3 + RIGHT * 2.25,
            stroke_color=RED_A,
            stroke_width=8,
        )
        c_language = LanguageModel("C: 指针").scale(0.5 * 1.5)
        c_language_ellipse = c_language.get_ellipse()
        c_language_label = c_language.get_label()
        c_language.next_to(assembly2c_arrow, UP, buff=0.12)

        self.play(GrowArrow(compiler2c_arrow))
        self.wait()
        self.play(GrowArrow(assembly2c_arrow))
        self.wait()
        self.play(FadeIn(c_language_ellipse))
        self.wait()
        self.play(Write(c_language_label))
        self.wait()

        c_language_rect = SurroundingRectangle(
            c_language_label, color=LIGHT_PINK, stroke_width=5, buff=0.7
        )
        pointer_explain_text = Text("指针仅存在于此", color=LIGHT_PINK).scale(0.8)
        pointer_explain_text.next_to(c_language_rect, RIGHT, buff=0.1)

        self.play(ShowCreation(c_language_rect))
        self.wait()
        self.play(Write(pointer_explain_text))
        self.wait()

        self.play(
            FadeOut(
                VGroup(
                    c_code_group,
                    assembly_code_arm_group,
                    assembly_code_riscv_group,
                    c_code_text,
                    assembly_code_arm_text,
                    assembly_code_riscv_text,
                )
            )
        )
        self.wait()

        assembly_compiler_group.add(
            c_language_rect,
            c_language,
            assembly2c_arrow,
            compiler2c_arrow,
            pointer_explain_text,
        )
        assembly_compiler_group.generate_target()
        assembly_compiler_group.target.scale(1 / 1.5).shift(UP + RIGHT * 0.6)
        self.play(MoveToTarget(assembly_compiler_group))
        self.wait()
        self.play(FadeIn(fade_out_group))
        self.wait()

        abstraction_arrow = Arrow(
            DOWN * 3.6,
            UP * 3.6,
            stroke_color=GOLD_B,
            stroke_width=4,
        ).shift(RIGHT * 4)
        abstraction_text = Text("层\n层\n抽\n象", color=GOLD_B).scale(0.8)
        abstraction_text.next_to(abstraction_arrow, RIGHT, buff=0.1)
        self.play(GrowFromEdge(abstraction_arrow, DOWN))
        self.wait()
        self.play(Write(abstraction_text))
        self.wait(2)
        self.play(FadeOut(c_language_rect), FadeOut(pointer_explain_text))
        self.wait()

        right_virtual_memory2java_arrow = Arrow(
            right_virtual_memory_rect.get_corner(UP) + DOWN * 0.12,
            right_virtual_memory_rect.get_corner(UP) + UP * 1.5,
            stroke_color=ORANGE,
            stroke_width=4,
        )

        java_language = LanguageModel("Java: 引用").scale(0.5)
        java_language.next_to(right_virtual_memory2java_arrow, UP, buff=0.12)

        jvm = MiddlewareModel("Java虚拟机", height=5).scale(0.6)
        jvm.get_label().shift(UP * 0.8)
        jvm.next_to(right_virtual_memory2java_arrow, UP, buff=0.12).shift(DOWN)

        self.play(GrowArrow(right_virtual_memory2java_arrow))
        self.wait()
        self.play(Write(java_language))
        self.wait()
        self.play(Write(jvm))
        self.wait()


# 废弃
class RefExplain(Scene):
    def construct(self) -> None:
        pointer_model = MemoryTableOnePointer().scale(0.8).move_to(ORIGIN)
        pointer_value_table = pointer_model.get_pointer_row().get_value_table()
        pointer_model_arrow = CurvedArrow(
            start_point=pointer_model.get_pointer_value_label().get_right()
            + RIGHT * 0.15,
            end_point=pointer_model.get_value_address0_label().get_right(),
            stroke_width=4,
            angle=TAU / 3,
        ).set_color(GOLD)
        change_text = Text("p = (int*)0xffffffffffff;", color=RED).scale(0.8)
        change_text.next_to(pointer_value_table, DOWN, buff=0.1)
        change_pointer_value_text = Text("0xffffffffffff", color=RED).scale(0.5)
        change_pointer_value_text.next_to(pointer_value_table.get_row_label(0), ORIGIN)
        change_pointer_model_arrow = CurvedArrow(
            start_point=change_pointer_value_text.get_right() + RIGHT * 0.15,
            end_point=pointer_model.get_value_address0_label().get_right() + UP * 10,
            stroke_width=4,
            angle=TAU / 10,
        ).set_color(RED)

        self.play(FadeIn(VGroup(pointer_model, pointer_model_arrow)))
        self.wait()
        self.play(Write(change_text))
        self.wait()
        self.play(
            ReplacementTransform(
                pointer_value_table.get_row_label(0), change_pointer_value_text
            )
        )
        self.wait()
        self.play(ReplacementTransform(pointer_model_arrow, change_pointer_model_arrow))
        self.wait()
        pointer_model_group = VGroup(
            pointer_model,
            change_text,
            change_pointer_value_text,
            change_pointer_model_arrow,
        )

        pointer_model_group.generate_target()
        pointer_model_group.target.scale(0.7).to_edge(UL).shift(RIGHT * 0.1 + UP * 4.8)
        divided_line = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=4)
        pointer_title = Text("指针(Pointer)", color=GOLD).scale(1.2)
        pointer_title.to_edge(UL).shift(DOWN * 0.1 + RIGHT * 0.1)

        self.play(MoveToTarget(pointer_model_group))
        self.wait()
        self.play(Write(pointer_title))
        self.wait()
        self.play(GrowFromCenter(divided_line))
        self.wait()

        reference_model = (
            MemoryTableReference()
            .scale(0.56)
            .to_edge(UR)
            .shift(LEFT * 0.2 + DOWN * 1.65)
        )
        reference_title = Text("C++引用(Reference)", color=GREEN).scale(1.2)
        reference_title.to_edge(UP).shift(DOWN * 0.1 + RIGHT * 2.8)
        reference_arrow = CurvedArrow(
            start_point=reference_model.get_reference_name_label().get_left()
            + LEFT * 0.1,
            end_point=reference_model.get_value_name_label().get_left(),
            stroke_width=4,
            angle=-TAU / 3,
        ).set_color(GREEN)
        reference_arrow_explain = Text("别名", color=GREEN).scale(0.8)
        reference_arrow_explain.next_to(reference_arrow, LEFT, buff=0.1)
        address_group = VGroup()
        for i in range(4):
            value_label = (
                reference_model.get_value_row().get_address_table().get_row_label(i)
            )
            address_group.add(value_label)

        for i in range(8):
            reference_label = (
                reference_model.get_reference_row().get_address_table().get_row_label(i)
            )
            address_group.add(reference_label)

        lock = (
            SVGMobject(svg_path + "lock.svg")
            .scale(0.5)
            .set_fill(WHITE, 1)
            .set_stroke(BLACK, 2.5, 1)
        )
        lock.next_to(
            reference_model.get_reference_row().get_value_table().get_row_label(0),
            ORIGIN,
        )

        self.play(Write(reference_title))
        self.wait()
        self.play(FadeIn(reference_model))
        self.wait()
        self.play(GrowArrow(reference_arrow))
        self.wait()
        self.play(Write(reference_arrow_explain))
        self.wait()
        self.play(FadeOut(address_group))
        self.wait()
        self.play(Write(lock))
        self.wait()


# 废弃
class JvmIntro(Scene):
    def construct(self) -> None:
        physical_memory = MemoryModel("物理内存", ": 物理地址").to_edge(DOWN).scale(0.6)
        physical_memory_rect = physical_memory.get_rect()

        physical_memory2operation_system_arrow = Arrow(
            physical_memory_rect.get_corner(UP) + DOWN * 0.12,
            physical_memory_rect.get_corner(UP) + UP * 1.5,
            stroke_width=3,
        )

        operation_system = MiddlewareModel("操作系统").scale(0.8)
        operation_system_rect = operation_system.get_rect()
        operation_system.next_to(physical_memory2operation_system_arrow, UP, buff=0.12)

        os2left_virtual_memory_arrow = Arrow(
            operation_system_rect.get_corner(UP) + DOWN * 0 + LEFT * 1,
            operation_system_rect.get_corner(UP) + UP * 1.5 + LEFT * 3,
            stroke_width=3,
        )

        os2right_virtual_memory_arrow = Arrow(
            operation_system_rect.get_corner(UP) + DOWN * 0 + RIGHT * 1,
            operation_system_rect.get_corner(UP) + UP * 1.5 + RIGHT * 3,
            stroke_width=3,
        )

        left_virtual_memory = MemoryModel("虚拟内存", ": 虚拟地址", width=8).scale(0.6)
        left_virtual_memory_rect = left_virtual_memory.get_rect()
        left_virtual_memory.next_to(os2left_virtual_memory_arrow, UP, buff=0.12).shift(
            LEFT * 0.9
        )

        right_virtual_memory = MemoryModel("虚拟内存", ": 虚拟地址", width=8).scale(0.6)
        right_virtual_memory_rect = right_virtual_memory.get_rect()
        right_virtual_memory.next_to(
            os2right_virtual_memory_arrow, UP, buff=0.12
        ).shift(RIGHT * 0.9)

        virtual_os_physical_group = (
            VGroup(
                operation_system,
                physical_memory,
                left_virtual_memory,
                right_virtual_memory,
                os2left_virtual_memory_arrow,
                os2right_virtual_memory_arrow,
                physical_memory2operation_system_arrow,
            )
            .scale(0.55)
            .to_edge(DOWN)
        )

        compiler = MiddlewareModel(
            "编\n译\n器",
            width=1,
            height=7,
        ).scale(0.5)
        compiler_rect = compiler.get_rect()

        compiler.next_to(left_virtual_memory_rect, LEFT, buff=0.4).shift(UP * 2.2)

        left_virtual_memory2assembly_arrow = Arrow(
            left_virtual_memory_rect.get_corner(UP) + DOWN * 0.12,
            left_virtual_memory_rect.get_corner(UP) + UP * 1,
            stroke_color=ORANGE,
            stroke_width=4,
        )

        compiler2assembly_arrow = Arrow(
            compiler_rect.get_corner(DR) + UP * 0.35,
            compiler_rect.get_corner(DR) + UP * 0.35 + RIGHT * 1.6,
            stroke_color=RED_A,
            stroke_width=8,
        )

        assembly_language = LanguageModel("汇编: 直接操作", text_scale=0.8).scale(0.5)
        assembly_language.next_to(left_virtual_memory2assembly_arrow, UP, buff=0.12)

        assembly2c_arrow = Arrow(
            assembly_language.get_corner(UP) + DOWN * 0.1,
            assembly_language.get_corner(UP) + UP * 1,
            stroke_color=ORANGE,
            stroke_width=4,
        )
        compiler2c_arrow = Arrow(
            compiler_rect.get_corner(UR) + DOWN * 1.5,
            compiler_rect.get_corner(UR) + DOWN * 1.5 + RIGHT * 1.6,
            stroke_color=RED_A,
            stroke_width=8,
        )
        c_language = LanguageModel("C: 指针").scale(0.5)
        c_language.next_to(assembly2c_arrow, UP, buff=0.12)

        previous_group = VGroup(
            compiler,
            left_virtual_memory2assembly_arrow,
            compiler2assembly_arrow,
            assembly_language,
            c_language,
            assembly2c_arrow,
            compiler2c_arrow,
            virtual_os_physical_group,
        )

        self.play(FadeIn(previous_group))
        self.wait()

        right_virtual_memory2java_arrow = Arrow(
            right_virtual_memory_rect.get_corner(UP) + DOWN * 0.12,
            right_virtual_memory_rect.get_corner(UP) + UP * 1.5,
            stroke_color=ORANGE,
            stroke_width=4,
        )

        java_language = LanguageModel("Java: 引用").scale(0.5)
        java_language.next_to(right_virtual_memory2java_arrow, UP, buff=0.12)

        jvm = MiddlewareModel("Java虚拟机", height=5).scale(0.6)
        jvm.get_label().shift(UP * 0.8)
        jvm.next_to(right_virtual_memory2java_arrow, UP, buff=0.12).shift(DOWN)

        abstraction_arrow = Arrow(
            DOWN * 3.6,
            UP * 3.6,
            stroke_color=GOLD_B,
            stroke_width=4,
        ).shift(RIGHT * 4)
        abstraction_text = Text("层\n层\n抽\n象", color=GOLD_B).scale(0.8)
        abstraction_text.next_to(abstraction_arrow, RIGHT, buff=0.1)
        self.play(GrowFromEdge(abstraction_arrow, DOWN))
        self.wait()
        self.play(Write(abstraction_text))
        self.wait(2)

        self.play(GrowArrow(right_virtual_memory2java_arrow))
        self.wait()
        self.play(Write(java_language))
        self.wait()
        self.play(Write(jvm))
        self.wait()


class JavaComparison(Scene):
    def construct(self) -> None:
        c_title = Text("C", color=GOLD).scale(1.5).to_edge(UL).shift(RIGHT * 0.3)

        code_c = (
            Code(
                code="""
        int arr[2] = {0, 1};
        int value = 2568;
        int x = arr[2];
        """,
                font="Fira",
                language="c",
            )
            .scale(2)
            .move_to(ORIGIN)
        )

        self.play(Write(c_title))
        self.wait()
        self.play(Write(code_c))
        self.wait()
        self.play(Indicate(code_c[-4:-1]))
        self.wait()

        memory_rect_c = (
            OneColTable(
                labels=["0", "1", "2568", ""],
                width=1.8,
                num_rows=4,
                show_label=True,
                text_scale=2.5,
            )
            .scale(0.8)
            .to_edge(LEFT)
            .shift(RIGHT * 2.2 + UP * 0.4)
        )
        memory_row0_label_c = Text("arr[0]", color=BLUE).scale(0.8)
        memory_row0_label_c.next_to(memory_rect_c.get_row_rect(0), RIGHT, buff=0.2)
        memory_row1_label_c = Text("arr[1]", color=BLUE).scale(0.8)
        memory_row1_label_c.next_to(memory_rect_c.get_row_rect(1), RIGHT, buff=0.2)
        memory_row2_label_c = Text("value", color=BLUE).scale(0.8)
        memory_row2_label_c.next_to(memory_rect_c.get_row_rect(2), RIGHT, buff=0.2)
        memory_label_c_group = VGroup(
            memory_row0_label_c, memory_row1_label_c, memory_row2_label_c
        )

        c_arrow = Arrow(
            memory_rect_c.get_row_rect(0).get_left() + LEFT * 1.5,
            memory_rect_c.get_row_rect(0).get_left() + RIGHT * 0.1,
            stroke_width=6,
        )

        memory_c_group = VGroup(
            memory_rect_c,
            memory_row0_label_c,
            memory_row1_label_c,
            memory_row2_label_c,
        )

        divide_line = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=2)

        code_c.generate_target()
        code_c.target.scale(0.7).next_to(memory_rect_c, DOWN, buff=0.7)

        java_title = Text("Java", color=GOLD).scale(1.5).to_edge(UR).shift(LEFT * 4.5)
        memory_java_group = memory_c_group.copy().to_edge(RIGHT).shift(LEFT * 1.5)
        java_arrow = Arrow(
            memory_java_group[0].get_row_rect(0).get_left() + LEFT * 1.5,
            memory_java_group[0].get_row_rect(0).get_left() + RIGHT * 0.1,
            stroke_width=6,
        )
        code_java = (
            Code(
                code="""
                int[] arr = {0, 1};
                int value = 2568;
                int x = arr[2];
                """,
                font="Fira",
                language="java",
            )
            .scale(1.4)
            .next_to(memory_java_group, DOWN, buff=0.7)
        )

        memory_java_rect = SurroundingRectangle(
            memory_java_group, color=YELLOW, stroke_width=2, buff=0.45
        )
        memory_java_rect_dashed = DashedVMobject(memory_java_rect, num_dashes=60)
        memory_java_rect_label = Text("JVM", color=YELLOW).scale(0.8)
        memory_java_rect_label.next_to(memory_java_rect, UP, buff=0.1)

        self.play(MoveToTarget(code_c))
        self.wait()
        self.play(FadeIn(memory_rect_c))
        self.wait()
        self.play(Write(memory_label_c_group))
        self.wait()
        self.play(GrowArrow(c_arrow))
        self.wait()
        self.play(GrowFromCenter(divide_line))
        self.wait()

        self.play(FadeIn(java_title))
        self.wait()
        self.play(ReplacementTransform(memory_c_group.copy(), memory_java_group))
        self.wait()
        self.play(GrowArrow(java_arrow))
        self.wait()
        self.play(Write(code_java))
        self.wait()
        self.play(ShowCreation(memory_java_rect_dashed))
        self.wait()
        self.play(Write(memory_java_rect_label))
        self.wait()

        c_arrow_1 = Arrow(
            memory_rect_c.get_row_rect(1).get_left() + LEFT * 1.5,
            memory_rect_c.get_row_rect(1).get_left() + RIGHT * 0.1,
            stroke_width=6,
        )
        self.play(FadeOut(c_arrow))
        self.wait()
        self.play(GrowArrow(c_arrow_1))
        self.wait()
        self.play(Indicate(memory_rect_c.get_row_label(1), scale_factor=2))
        self.wait()

        java_arrow_10 = Arrow(
            memory_java_group[0].get_row_rect(1).get_left() + LEFT * 1.5,
            memory_java_group[0].get_row_rect(1).get_left() + LEFT * 0.28,
            stroke_width=6,
        )
        java_arrow_11 = Arrow(
            memory_java_group[0].get_row_rect(1).get_left() + LEFT * 1.5,
            memory_java_group[0].get_row_rect(1).get_left() + RIGHT * 0.1,
            stroke_width=6,
        )
        self.play(FadeOut(java_arrow))
        self.wait()
        self.play(GrowArrow(java_arrow_10))
        self.wait()
        self.play(FlashAround(memory_java_rect_dashed), run_time=2)
        self.wait()
        self.play(ReplacementTransform(java_arrow_10, java_arrow_11))
        self.wait()
        self.play(Indicate(memory_java_group[0].get_row_label(1), scale_factor=2))
        self.wait()

        c_arrow_2 = Arrow(
            memory_rect_c.get_row_rect(2).get_left() + LEFT * 1.5,
            memory_rect_c.get_row_rect(2).get_left() + RIGHT * 0.1,
            stroke_width=6,
        )
        self.play(FadeOut(c_arrow_1))
        self.wait()
        self.play(GrowArrow(c_arrow_2))
        self.wait()
        self.play(Indicate(memory_rect_c.get_row_label(2), scale_factor=2))
        self.wait()

        java_arrow_20 = Arrow(
            memory_java_group[0].get_row_rect(2).get_left() + LEFT * 1.5,
            memory_java_group[0].get_row_rect(2).get_left() + LEFT * 0.28,
            stroke_width=6,
        )
        expection_text = Text("ArrayIndexOutOfBoundsException", color=RED).scale(0.7)
        expection_text.next_to(java_arrow_20, DOWN, buff=0.5).shift(RIGHT * 1)

        self.play(FadeOut(java_arrow_11))
        self.wait()
        self.play(GrowArrow(java_arrow_20))
        self.wait()
        self.play(FlashAround(memory_java_rect_dashed), run_time=2)
        self.wait()
        self.play(Write(expection_text))
        self.wait()

        self.clear()


class CircleAbstract(Scene):
    def construct(self) -> None:
        hardware_text = Text("计算机硬件", color=WHITE).scale(4)
        self.play(Write(hardware_text))
        self.wait()

        radius = 3.5
        circle = Circle(radius=radius)
        # start_angle_a = 3 * PI / 4  # 左上角
        # start_angle_b = 7 * PI / 4  # 右下角
        start_angle_a = PI
        start_angle_b = 0

        point_a = Dot().scale(0.2).move_to(circle.point_at_angle(start_angle_a))
        point_b = Dot().scale(0.2).move_to(circle.point_at_angle(start_angle_b))

        trail_a = VMobject(stroke_width=4)
        trail_a.set_points_as_corners([point_a.get_center(), point_a.get_center()])
        trail_b = VMobject(stroke_width=4)
        trail_b.set_points_as_corners([point_b.get_center(), point_b.get_center()])

        def update_trail_a(trail):
            trail.add_points_as_corners([point_a.get_center()])

        def update_trail_b(trail):
            trail.add_points_as_corners([point_b.get_center()])

        trail_a.add_updater(update_trail_a)
        trail_b.add_updater(update_trail_b)

        self.add(trail_a, trail_b)
        self.play(
            Rotate(point_a, angle=PI, about_point=ORIGIN),
            Rotate(point_b, angle=PI, about_point=ORIGIN),
            run_time=3,
            rate_func=rush_from,
        )
        self.play(FadeOut(point_a), FadeOut(point_b))
        trail_a.clear_updaters()
        trail_b.clear_updaters()
        self.wait()

        hardware_text.generate_target()
        hardware_text.target.to_edge(DOWN).shift(DOWN * 0.1).scale(0.25)
        self.play(MoveToTarget(hardware_text))
        self.wait()

        compiler_circle = CompilerCircle().scale(0.45)
        c_text = Text("C语言", color=WHITE)
        compiler_text = Text("编译器", color=GREEN_B).scale(0.8)
        compiler_text.next_to(compiler_circle, UP, buff=0.1).shift(UP * 0.3)

        arrow = Arrow(
            c_text.get_corner(DOWN),
            hardware_text.get_corner(UP),
            stroke_color=ORANGE,
            stroke_width=4,
        )
        arrow_text = Text("指针", color=ORANGE).scale(0.75)
        arrow_text.next_to(arrow, RIGHT, buff=0.1).shift(UP * 0.6)

        end_length = 0.8
        angles = np.array([np.pi / 4, 3 * np.pi / 4, 5 * np.pi / 4, 7 * np.pi / 4])
        end_points = np.array(
            [
                (end_length * np.cos(angle), end_length * np.sin(angle))
                for angle in angles
            ]
        )

        arrow_width = 15
        arrow_color = LIGHT_PINK
        arrow_start_scale = 2.2
        arrow_ur = Arrow(
            arrow_start_scale * UR,
            end_points[0],
            stroke_width=arrow_width,
            stroke_color=arrow_color,
        )
        arrow_ul = Arrow(
            arrow_start_scale * UL,
            end_points[1],
            stroke_width=arrow_width,
            stroke_color=arrow_color,
        )
        arrow_dl = Arrow(
            arrow_start_scale * DL,
            end_points[2],
            stroke_width=arrow_width,
            stroke_color=arrow_color,
        )
        arrow_dr = Arrow(
            arrow_start_scale * DR,
            end_points[3],
            stroke_width=arrow_width,
            stroke_color=arrow_color,
        )

        ur_label = Text("汇编").scale(0.8)
        ur_label.next_to(arrow_ur, RIGHT, buff=0.1)
        ul_label = Text("内存").scale(0.8)
        ul_label.next_to(arrow_ul, LEFT, buff=0.1)
        dl_label = Text("CPU").scale(0.8)
        dl_label.next_to(arrow_dl, LEFT, buff=0.1)
        dr_label = Text("I/O").scale(0.8)
        dr_label.next_to(arrow_dr, RIGHT, buff=0.1)

        self.play(Write(compiler_circle), run_time=2)
        self.wait()

        def complex_func(z: complex, t: float) -> complex:
            return interpolate(z, z**3, t)

        self.play(ComplexHomotopy(complex_func, compiler_circle))
        self.wait()
        self.play(Write(compiler_text))
        self.wait()
        self.play(Write(c_text))
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(Write(arrow_text))
        self.wait(2)
        self.play(
            GrowArrow(arrow_ur),
            GrowArrow(arrow_ul),
            GrowArrow(arrow_dr),
            GrowArrow(arrow_dl),
        )
        self.wait()
        self.play(Write(ur_label), Write(ul_label), Write(dl_label), Write(dr_label))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    arrow_ur,
                    arrow_ul,
                    arrow_dr,
                    arrow_dl,
                    ur_label,
                    ul_label,
                    dl_label,
                    dr_label,
                )
            )
        )
        self.wait()
        self.clear()


class Cover(Scene):
    def construct(self) -> None:
        title = (
            Text("C语言指针", color=YELLOW)
            .scale(3)
            .to_edge(UL, buff=0.8)
            .shift(RIGHT * 0.2)
        )

        trick = (
            Text(
                """
                     基础知识

                     块的概念

                     映射策略

                     缓存结构
                     """,
                color=LIGHT_PINK,
            )
            .scale(1.2)
            .to_edge(DR, buff=0.8)
            .shift(LEFT * 2 + UP * 0.4)
        )
        group = VGroup(title, trick)
        group.scale(1).shift(RIGHT * 1.2)
        self.add(title)
        # self.add(trick)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = f"manimgl {module_name} JavaComparison -ow"
    os.system(command)
