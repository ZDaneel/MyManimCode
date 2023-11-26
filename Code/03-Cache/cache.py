from manimlib import *
import numpy as np

svg_path = "./images/svg/"


class CacheIntroduction(Scene):
    def construct(self):
        title = Text("缓存(Cache)", color=MAROON_B).scale(1.5)
        title.to_edge(UP + LEFT)

        intel_chip_text = Text("Intel I7芯片架构", color=BLUE).scale(1.2)
        intel_chip_text.move_to(ORIGIN).shift(UP * 2)
        intel_chip_image = ImageMobject("intel-chip.png")
        intel_chip_image.next_to(intel_chip_text, DOWN, buff=0.4)

        apple_chip_text = Text("Apple M系列芯片架构", color=BLUE).scale(1.2)
        apple_chip_text.move_to(ORIGIN).shift(UP * 2)
        apple_chip_image = ImageMobject("m-chip.png").scale(1.2)
        apple_chip_image.next_to(apple_chip_text, DOWN, buff=0.4)

        inter_chip_rect = Rectangle(color=ORANGE, height=1.1, width=5).shift(DOWN)
        apple_chip_rect = Rectangle(color=GREEN, height=1, width=2.8).shift(
            DOWN * 2.5 + LEFT * 0.59
        )

        self.play(Write(title), run_time=2)
        self.wait()
        self.play(Write(intel_chip_text), FadeIn(intel_chip_image))
        self.wait()
        self.play(ShowCreation(inter_chip_rect))
        self.wait(2)
        self.play(
            FadeOut(intel_chip_text),
            FadeOut(intel_chip_image),
            FadeOut(inter_chip_rect),
        )
        self.wait()
        self.play(Write(apple_chip_text), FadeIn(apple_chip_image))
        self.wait()
        self.play(ShowCreation(apple_chip_rect))
        self.wait(2)
        self.play(
            FadeOut(apple_chip_text),
            FadeOut(apple_chip_image),
            FadeOut(apple_chip_rect),
            FadeOut(title),
        )
        self.wait()

        xt = (
            SVGMobject(svg_path + "qxt.svg")
            .scale(3.2)
            .set_fill(BLACK, 1)
            .set_stroke(WHITE, 2.5, 1)
        )
        qxx = (
            SVGMobject(svg_path + "qxx.svg")
            .scale(1)
            .set_fill(BLACK, 1)
            .set_stroke(WHITE, 2.5, 1)
        ).to_edge(DL)
        qxx_1 = qxx.copy().next_to(qxx, RIGHT, buff=0.1)
        qxx_2 = qxx.copy().next_to(qxx_1, RIGHT, buff=0.2)

        bubble = Bubble(height=4, width=6, direction=RIGHT).shift(UP * 0.2)
        text = (
            Text(
                """
        缓存的基础知识
            """
            )
            .scale(1.2)
            .shift(LEFT * 0.1 + UP * 0.2)
        )

        intro_rect = (
            Rectangle(height=9 / 2, width=16 / 2)
            .set_fill(BLACK, opacity=1)
            .to_edge(UL)
            .shift(DOWN * 0.42 + RIGHT * 0.6)
        )
        title_1 = Text("1. 什么是缓存", color=BLUE).scale(0.8).next_to(intro_rect, UP)
        title_2 = Text("2. 块的概念", color=BLUE).scale(0.8).next_to(intro_rect, UP)
        title_3 = Text("3. 缓存映射", color=BLUE).scale(0.8).next_to(intro_rect, UP)
        title_4 = Text("4. 缓存结构", color=BLUE).scale(0.8).next_to(intro_rect, UP)

        self.play(ShowCreation(xt), run_time=1)
        xt.generate_target()
        xt.target.scale(0.65).to_edge(DR).shift(LEFT * 0.4 + DOWN * 0.1)
        self.play(MoveToTarget(xt), run_time=1)
        self.wait()
        self.play(ShowCreation(qxx), ShowCreation(qxx_1), ShowCreation(qxx_2))
        self.wait()
        self.play(ShowCreation(bubble), Write(text))
        self.wait()
        self.play(FadeOut(bubble), FadeOut(text))
        self.wait()
        self.play(ShowCreation(intro_rect), Write(title_1))
        self.wait()
        self.play(ReplacementTransform(title_1, title_2))
        self.wait()
        self.play(ReplacementTransform(title_2, title_3))
        self.wait()
        self.play(ReplacementTransform(title_3, title_4))
        self.wait()
        self.play(
            FadeOut(intro_rect),
            FadeOut(title_4),
            FadeOut(xt),
            FadeOut(qxx),
            FadeOut(qxx_1),
            FadeOut(qxx_2),
        )


class CacheBasics(Scene):
    def construct(self) -> None:
        title = Text("缓存(Cache)", color=MAROON_B).scale(1.5)
        title.to_edge(UP + LEFT)

        axes = (
            Axes(
                x_range=[0, 6],
                y_range=[0, 7],
                axis_config={"color": WHITE, "include_tip": True},
            )
            .scale(0.8)
            .shift(RIGHT * 2)
        )

        x_label = Text("时间").scale(0.7).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("地址").scale(0.7).next_to(axes.y_axis.get_top(), RIGHT)
        labels = VGroup(x_label, y_label)

        scalar_dots = VGroup(
            *[Dot(axes.c2p(t, 1), fill_color=BLUE) for t in np.linspace(1, 5, 5)]
        )

        start_point = np.array([1, 2, 0])
        end_point = np.array([5, 6, 0])
        number_of_dots = 5
        dot_positions = [
            interpolate(start_point, end_point, alpha)
            for alpha in np.linspace(0, 1, number_of_dots)
        ]
        array_dots = VGroup(
            *[
                Dot(axes.c2p(position[0], position[1]), fill_color=RED)
                for position in dot_positions
            ]
        )
        all_dots = VGroup(scalar_dots, array_dots)

        scalar_dots_label = (
            Text("标量访问", color=BLUE)
            .next_to(scalar_dots, LEFT, buff=1)
            .shift(LEFT + UP * 0.5)
        )
        array_dots_label = (
            Text("数组访问", color=RED).next_to(array_dots, LEFT, buff=1).shift(LEFT + UP)
        )

        scalar_code_str = "a = 10\nfor i in range(5):\n    print(a)"
        scalar_code = (
            Code(
                code=scalar_code_str,
                font="Fira",
            )
            .scale(1.2)
            .next_to(scalar_dots_label, DOWN, buff=0.2)
        )
        scalar_code_rect = SurroundingRectangle(
            scalar_code, color=YELLOW, stroke_width=1
        )

        array_code_str = "arr = [1, 2, 3, 4, 5]\nfor i in range(5):\n    print(arr[i])"
        array_code = (
            Code(
                code=array_code_str,
                font="Fira",
            )
            .scale(1.2)
            .next_to(array_dots_label, DOWN, buff=0.2)
        )
        array_code_rect = SurroundingRectangle(array_code, color=YELLOW, stroke_width=1)

        locality_principle_text = (
            Text("局部性原理", color=GREEN_B).scale(1.5).next_to(axes, ORIGIN)
        )

        self.play(Write(title))
        self.wait()
        self.play(ShowCreation(axes))
        self.wait()
        self.play(Write(x_label))
        self.wait()
        self.play(Write(y_label))
        self.wait()
        self.play(Write(scalar_dots_label))
        self.wait()
        self.play(Write(scalar_code), ShowCreation(scalar_code_rect))
        self.wait()
        self.play(ShowCreation(scalar_dots), run_time=2)
        self.wait()
        self.play(Write(array_dots_label))
        self.wait()
        self.play(Write(array_code), ShowCreation(array_code_rect))
        self.wait()
        self.play(ShowCreation(array_dots), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(all_dots, locality_principle_text))
        self.wait()
        locality_principle_text.generate_target()
        locality_principle_text.target.shift(UP * 1.5)
        time_locality_text = (
            Text("时间局部性", color=YELLOW_D)
            .scale(1.2)
            .next_to(locality_principle_text.target, DOWN, buff=0.5)
            .align_to(locality_principle_text.target, LEFT)
            .shift(RIGHT * 1)
        )
        space_locality_text = (
            Text("空间局部性", color=YELLOW_D)
            .scale(1.2)
            .next_to(time_locality_text, DOWN, buff=0.3)
            .align_to(time_locality_text, LEFT)
        )
        self.play(MoveToTarget(locality_principle_text))
        self.wait()
        self.play(Write(time_locality_text))
        self.wait()
        self.play(Write(space_locality_text))
        self.wait(2)

        self.play(
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(scalar_dots_label),
            FadeOut(scalar_code),
            FadeOut(scalar_code_rect),
            FadeOut(array_dots_label),
            FadeOut(array_code),
            FadeOut(array_code_rect),
            FadeOut(locality_principle_text),
            FadeOut(time_locality_text),
            FadeOut(space_locality_text),
        )

        mem_text = Text("读取数据", color=TEAL_A).scale(1)
        mem_text.next_to(title, DOWN, buff=0.4).align_to(title, LEFT)

        # 创建CPU矩形
        cpu_rect = Rectangle(height=2, width=2)
        cpu_text = Text("CPU")
        cpu_text.move_to(cpu_rect.get_center())
        cpu_group = VGroup(cpu_rect, cpu_text)

        # 创建Memory矩形
        memory_rect = Rectangle(height=4, width=3)
        memory_text = Text("Memory")
        memory_text.move_to(memory_rect.get_center())
        memory_group = VGroup(memory_rect, memory_text)

        # 将CPU和Memory放置到合适的位置
        cpu_group.to_edge(LEFT, buff=3)
        memory_group.to_edge(RIGHT, buff=3)

        # 创建从CPU到Memory的箭头并添加"Address"标签
        address_arrow = Arrow(
            cpu_rect.get_right() + UP * 0.5,
            memory_rect.get_left() + UP * 0.5,
            buff=0.3,
            stroke_color=ORANGE,
        )
        address_label = Text("Address").set_color(ORANGE).next_to(address_arrow, UP)

        # 创建从Memory到CPU的箭头并添加"Data"标签
        data_arrow = Arrow(
            memory_rect.get_left() + DOWN * 0.5,
            cpu_rect.get_right() + DOWN * 0.5,
            buff=0.3,
            stroke_color=BLUE,
        )
        data_label = Text("Data").set_color(BLUE).next_to(data_arrow, DOWN)

        # 添加所有元素到场景
        self.play(ShowCreation(cpu_rect))
        self.wait()
        self.play(Write(cpu_text))
        self.wait()
        self.play(ShowCreation(memory_rect))
        self.wait()
        self.play(Write(memory_text))
        self.wait()
        self.play(Write(mem_text))
        self.wait()
        self.play(ShowCreation(address_arrow), Write(address_label))
        self.play(ShowCreation(data_arrow), Write(data_label))
        self.wait()

        # 删除CPU和Memory的箭头和标签
        self.play(
            FadeOut(address_arrow),
            FadeOut(address_label),
            FadeOut(data_arrow),
            FadeOut(data_label),
        )
        self.wait()

        # 上下分别创建容量和速度的渐变箭头
        capacity_arrow = Arrow(
            cpu_rect.get_top() + UP * 0.4,
            memory_rect.get_top() + UP * 0.7,
            buff=0.2,
        ).set_color_by_gradient(TEAL_A, ORANGE)
        capacity_label = (
            Text("容量").set_color(RED).next_to(capacity_arrow, UP, buff=0.05)
        )
        speed_arrow = Arrow(
            cpu_rect.get_bottom() + DOWN * 0.4,
            memory_rect.get_bottom() + DOWN * 0.7,
            buff=0.2,
        ).set_color_by_gradient(BLUE_B, RED_C)
        speed_label = Text("速度").set_color(GREEN).next_to(speed_arrow, DOWN, buff=0.05)

        self.play(ShowCreation(capacity_arrow), Write(capacity_label))
        self.wait()
        self.play(ShowCreation(speed_arrow), Write(speed_label))
        self.wait()

        cpu_group.generate_target()
        memory_group.generate_target()
        capacity_arrow.generate_target()
        speed_arrow.generate_target()
        cpu_group.target.shift(LEFT * 1.8)
        memory_group.target.shift(RIGHT * 1.8)
        capacity_arrow.target.put_start_and_end_on(
            cpu_group.target.get_top() + UP * 0.4,
            memory_group.target.get_top() + UP * 0.7,
        )
        speed_arrow.target.put_start_and_end_on(
            cpu_group.target.get_bottom() + DOWN * 0.4,
            memory_group.target.get_bottom() + DOWN * 0.7,
        )
        self.play(
            MoveToTarget(cpu_group),
            MoveToTarget(memory_group),
            MoveToTarget(capacity_arrow),
            MoveToTarget(speed_arrow),
        )
        self.wait()

        # 创建Cache矩形
        cache_rect = Rectangle(height=2.5, width=2.5)
        cache_text = Text("Cache")
        cache_text.move_to(cache_rect.get_center())
        cache_group = VGroup(cache_rect, cache_text)

        # 将Cache放置到CPU和Memory之间
        cache_group.move_to((cpu_group.get_right() + memory_group.get_left()) / 2)

        self.play(ShowCreation(cache_rect))
        self.wait()
        self.play(Write(cache_text))
        self.wait()
        self.play(Indicate(cache_group))
        self.wait()
        self.play(
            FadeOut(capacity_arrow),
            FadeOut(capacity_label),
            FadeOut(speed_arrow),
            FadeOut(speed_label),
        )
        self.wait()

        # 创建从CPU到Cache的箭头并添加"Address"标签
        cpu2cache_address_arrow = Arrow(
            cpu_rect.get_right() + UP * 0.3,
            cache_rect.get_left() + UP * 0.3,
            buff=0.2,
            stroke_color=ORANGE,
        )
        cpu2cache_address_label = (
            Text("Address").set_color(ORANGE).next_to(cpu2cache_address_arrow, UP)
        )

        # 创建从Cache到CPU的箭头并添加"Data"标签
        cache2cpu_data_arrow = Arrow(
            cache_rect.get_left() + DOWN * 0.3,
            cpu_rect.get_right() + DOWN * 0.3,
            buff=0.2,
            stroke_color=BLUE,
        )
        cache2cpu_data_label = (
            Text("Data").set_color(BLUE).next_to(cache2cpu_data_arrow, DOWN)
        )

        # 创建从Cache到Memory的箭头并添加"Address"标签
        cache2memory_address_arrow = Arrow(
            cache_rect.get_right() + UP * 0.3,
            memory_rect.get_left() + UP * 0.3,
            buff=0.2,
            stroke_color=ORANGE,
        )
        cache2memory_address_label = (
            Text("Address").set_color(ORANGE).next_to(cache2memory_address_arrow, UP)
        )

        # 创建从Memory到Cache的箭头并添加"Data"标签
        memory2cache_data_arrow = Arrow(
            memory_rect.get_left() + DOWN * 0.3,
            cache_rect.get_right() + DOWN * 0.3,
            buff=0.2,
            stroke_color=BLUE,
        )
        memory2cache_data_label = (
            Text("Data").set_color(BLUE).next_to(memory2cache_data_arrow, DOWN)
        )

        # Cache中有数据
        condition_text = Text("Cache中有数据", color=YELLOW_B).scale(1.2)
        terminology_text = Text("Cache Hit(命中)", color=YELLOW_B).scale(1.2)
        condition_text.next_to(cache_group, UP, buff=0.5).align_to(cache_group, ORIGIN)
        terminology_text.next_to(cache_group, UP, buff=0.5).align_to(
            cache_group, ORIGIN
        )
        self.play(Write(condition_text))
        self.wait()
        self.play(ShowCreation(cpu2cache_address_arrow), Write(cpu2cache_address_label))
        self.wait()
        self.play(ShowCreation(cache2cpu_data_arrow), Write(cache2cpu_data_label))
        self.wait()
        self.play(Transform(condition_text, terminology_text))
        self.wait()

        self.wait(2)
        self.play(
            FadeOut(cpu2cache_address_arrow),
            FadeOut(cpu2cache_address_label),
            FadeOut(cache2cpu_data_arrow),
            FadeOut(cache2cpu_data_label),
            FadeOut(condition_text),
            FadeOut(terminology_text),
        )
        self.wait()

        # Cache中没有数据
        condition_text = Text("Cache中没有数据", color=YELLOW_B).scale(1.2)
        terminology_text = Text("Cache Miss(丢失)", color=YELLOW_B).scale(1.2)
        condition_text.next_to(cache_group, UP, buff=0.5).align_to(cache_group, ORIGIN)
        terminology_text.next_to(cache_group, UP, buff=0.5).align_to(
            cache_group, ORIGIN
        )
        self.play(Write(condition_text))
        self.wait()
        self.play(ShowCreation(cpu2cache_address_arrow), Write(cpu2cache_address_label))
        self.wait()
        self.play(
            ShowCreation(cache2memory_address_arrow), Write(cache2memory_address_label)
        )
        self.wait()
        self.play(ShowCreation(memory2cache_data_arrow), Write(memory2cache_data_label))
        self.wait()
        self.play(ShowCreation(cache2cpu_data_arrow), Write(cache2cpu_data_label))
        self.wait()
        self.play(Transform(condition_text, terminology_text))
        self.wait()

        self.play(
            FadeOut(cpu2cache_address_arrow),
            FadeOut(cpu2cache_address_label),
            FadeOut(cache2memory_address_arrow),
            FadeOut(cache2memory_address_label),
            FadeOut(memory2cache_data_arrow),
            FadeOut(memory2cache_data_label),
            FadeOut(cache2cpu_data_arrow),
            FadeOut(cache2cpu_data_label),
            FadeOut(condition_text),
            FadeOut(terminology_text),
            FadeOut(title),
            FadeOut(mem_text),
            FadeOut(cpu_group),
            FadeOut(memory_group),
            FadeOut(cache_group),
        )


class CacheBlock(Scene):
    def construct(self) -> None:
        # 创建16x4的内存矩形网格
        memory_table = VGroup()
        memory_table_rect = VGroup()
        memory_table_label = VGroup()
        row_labels = VGroup()
        for i in range(16):
            for j in range(4):
                rect = Rectangle(height=0.45, width=0.45)
                rect.shift(RIGHT * j * 0.45 + DOWN * i * 0.45)
                label = Text(str(i * 4 + j), font_size=15, color=BLUE_C).move_to(
                    rect.get_corner(DOWN + RIGHT) + UP * 0.1 + LEFT * 0.1
                )
                memory_table_rect.add(rect)
                memory_table_label.add(label)

            # 添加行号标签
            row_label = Text(str(i), font_size=15, color=ORANGE)
            row_label.next_to(memory_table_rect[i * 4], LEFT).shift(DOWN * 0.1)
            row_labels.add(row_label)
        memory_table.add(memory_table_rect, memory_table_label, row_labels)
        memory_table.to_edge(UP, buff=0.3).shift(LEFT * 0.5)
        self.play(FadeIn(memory_table))
        self.wait()

        # 创建文本：内存大小为64B
        memory_size_text = Text("内存大小: 64B").to_edge(UP + LEFT).scale(1.2)
        self.play(Write(memory_size_text))
        self.wait()
        byte_addressed_text = (
            Text("按字节编址")
            .scale(0.9)
            .next_to(memory_size_text, DOWN, buff=0.2)
            .align_to(memory_size_text, LEFT)
        )
        self.play(Write(byte_addressed_text))
        self.wait()
        byte_line_text = (
            Text("""1"格"(Grid) 为 1字节(Byte)""", color=YELLOW, t2c={"格": RED})
            .scale(0.7)
            .next_to(byte_addressed_text, DOWN, buff=0.15)
            .align_to(byte_addressed_text, LEFT)
        )
        self.play(Write(byte_line_text))
        self.wait()
        explanation = (
            Text('6位<=>64个"格"', t2c={"6": BLUE_A, "64": RED_A, "格": RED})
            .next_to(byte_line_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(byte_line_text, LEFT)
        )
        self.play(Write(explanation))

        bit_table_6 = VGroup()
        for i in range(6):
            bit_rect = Rectangle(height=0.6, width=0.6)
            bit_label = (
                Text("0", color=YELLOW).scale(0.5).move_to(bit_rect.get_center())
            )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(explanation, DOWN, buff=0.1)
            else:
                bit.next_to(bit_table_6[-1], RIGHT, buff=0)
            bit_table_6.add(bit)

        bit_table_6.align_to(explanation, LEFT)

        self.play(FadeIn(bit_table_6))
        self.wait()

        # 介绍字的概念
        word_addressed_text = (
            Text("按字编址")
            .scale(0.9)
            .next_to(bit_table_6, DOWN, buff=0.5)
            .align_to(bit_table_6, LEFT)
        )
        self.play(Write(word_addressed_text))
        self.wait()

        word_byte_text_1 = (
            Text("1字(Word) = 4字节(Byte)", color=RED_D)
            .scale(0.7)
            .next_to(word_addressed_text, DOWN, buff=0.15)
            .align_to(word_addressed_text, LEFT)
        )
        self.play(Write(word_byte_text_1))
        self.wait()

        word_line_text = (
            Text('1"行"(line) 为 1字(Word)', color=YELLOW, t2c={"行": PURPLE_B})
            .scale(0.7)
            .next_to(word_byte_text_1, DOWN, buff=0.15)
            .align_to(word_byte_text_1, LEFT)
        )
        self.play(Write(word_line_text))
        self.wait()

        explanation_word = (
            Text('4位<=>16个"行"', t2c={"4": BLUE_A, "16": RED_A, "行": PURPLE_B})
            .next_to(word_line_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(word_line_text, LEFT)
        )
        self.play(Write(explanation_word))

        bit_table_4 = VGroup()
        for i in range(4):
            bit_rect = Rectangle(height=0.6, width=0.6)
            bit_label = (
                Text("0", color=YELLOW).scale(0.5).move_to(bit_rect.get_center())
            )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(explanation_word, DOWN, buff=0.1)
            else:
                bit.next_to(bit_table_4[-1], RIGHT, buff=0)
            bit_table_4.add(bit)

        bit_table_4.align_to(explanation_word, LEFT)

        self.play(FadeIn(bit_table_4))
        self.wait(2)

        memory_table.generate_target()
        memory_table.target.shift(LEFT)
        self.play(MoveToTarget(memory_table))

        # 右上角引入块的概念
        block_text_1 = (
            Text("1块(Block)=1字(Word)=4字节(Byte)", color=RED)
            .scale(0.6)
            .to_edge(UP + RIGHT, buff=0.4)
        )
        self.play(Write(block_text_1))
        self.wait()

        block_line_text_1 = (
            Text("""1"内存行"(Memory Line) 为 1块(Block)""", color=YELLOW)
            .scale(0.5)
            .next_to(block_text_1, DOWN, buff=0.2)
            .align_to(block_text_1, LEFT)
        )
        self.play(Write(block_line_text_1))
        for i in range(4):
            self.play(FlashAround(memory_table_rect[i * 4 : (i + 1) * 4]))
        self.wait()

        cache_line_text_1 = (
            Text("1缓存行(Cache Line)=1块(Block)", color=BLUE_D)
            .scale(0.5)
            .next_to(block_line_text_1, DOWN, buff=0.1)
            .align_to(block_line_text_1, LEFT)
        )

        # 给出四行的cache模型
        cache_table = VGroup()
        for i in range(4):
            rect = Rectangle(height=0.5, width=2)
            rect.shift(UP * i * 0.5)
            label = Text(str(i), font_size=15, color=YELLOW).next_to(rect, LEFT)
            cell_group = VGroup(rect, label)
            cache_table.add(cell_group)
        cache_table.arrange(DOWN, aligned_edge=RIGHT, buff=0)
        cache_table.next_to(cache_line_text_1, DOWN, buff=0.2).align_to(
            cache_line_text_1, LEFT
        )
        self.play(FadeIn(cache_table))
        self.wait()
        self.play(FlashAround(cache_table[0]))
        self.play(Write(cache_line_text_1))
        self.wait()

        # 闪烁一行，指向cache的每一行
        self.play(FlashAround(memory_table_rect[0:4]))
        cache_line_arrow = Arrow(
            memory_table_rect[0:4].get_right(),
            cache_table[0].get_left(),
            buff=0.2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(cache_line_arrow))

        for i in range(1, 4):
            # 创建一个新的目标位置
            new_end = cache_table[i].get_left() + LEFT * 0.2
            # 更新箭头的目标终点
            cache_line_arrow.generate_target()
            cache_line_arrow.target.put_start_and_end_on(
                cache_line_arrow.get_start(), new_end
            )
            # 沿着新的终点移动箭头
            self.play(MoveToTarget(cache_line_arrow), run_time=0.6)
        self.wait()
        self.play(FadeOut(cache_line_arrow))

        self.play(FlashAround(memory_table_rect[40:44]))
        cache_line_arrow = Arrow(
            memory_table_rect[40:44].get_right(),
            cache_table[0].get_left(),
            buff=0.2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(cache_line_arrow))
        for i in range(1, 4):
            # 创建一个新的目标位置
            new_end = cache_table[i].get_left() + LEFT * 0.2
            # 更新箭头的目标终点
            cache_line_arrow.generate_target()
            cache_line_arrow.target.put_start_and_end_on(
                cache_line_arrow.get_start(), new_end
            )
            # 沿着新的终点移动箭头
            self.play(MoveToTarget(cache_line_arrow), run_time=0.6)
        self.wait()
        self.play(FadeOut(cache_line_arrow))

        block_text_2 = (
            Text("1块(Block)=4字(Word)=16字节(Byte)", color=RED)
            .scale(0.6)
            .next_to(cache_table, DOWN, buff=0.8)
            .align_to(cache_table, LEFT)
        )
        self.play(Write(block_text_2))
        self.wait()

        block_line_text_2 = (
            Text("""4"内存行"(Memory Line) 为 1块(Block)""", color=YELLOW)
            .scale(0.5)
            .next_to(block_text_2, DOWN, buff=0.2)
            .align_to(block_text_2, LEFT)
        )
        self.play(Write(block_line_text_2))
        self.wait()

        for i in range(0, 16, 4):
            four_rows_group = VGroup(
                *[
                    memory_table_rect[k * 4 + j]
                    for k in range(i, i + 4)
                    for j in range(4)
                ]
            )
            self.play(FlashAround(four_rows_group))
        self.wait()

        cache_line_text_2 = (
            Text("1缓存行(Cache Line)=1块(Block)", color=BLUE_D)
            .scale(0.5)
            .next_to(block_line_text_2, DOWN, buff=0.15)
            .align_to(block_line_text_2, LEFT)
        )

        cache_table_2 = VGroup()
        for i in range(2):
            rect = Rectangle(height=0.5, width=2)
            rect.shift(UP * i * 0.5)
            label = Text(str(i), font_size=15, color=YELLOW).next_to(rect, LEFT)
            cell_group = VGroup(rect, label)
            cache_table_2.add(cell_group)
        cache_table_2.arrange(DOWN, aligned_edge=RIGHT, buff=0)
        cache_table_2.next_to(cache_line_text_2, DOWN, buff=0.2).align_to(
            cache_line_text_2, LEFT
        )

        colors = [RED, BLUE, GREEN, YELLOW]
        labels = ["0", "1", "2", "3"]
        group_rects = VGroup()
        group_rect_labels = VGroup()
        for index, color in enumerate(colors):
            group_rect = Rectangle(
                height=4 * 0.45,
                width=4 * 0.45,
                fill_opacity=0,
                stroke_color=color,
                stroke_width=4,
            )
            group_rect.move_to(
                memory_table_rect[4 * 4 * index].get_center()
                + DOWN * (3 * 0.45 / 2)
                + RIGHT * (0.68)
            )
            group_rect_label = (
                Text(labels[index], color=color)
                .scale(0.5)
                .next_to(group_rect, RIGHT, buff=0.2)
            )
            group_rects.add(group_rect)
            group_rect_labels.add(group_rect_label)
        self.play(ShowCreation(group_rects), Write(group_rect_labels))
        self.wait()
        self.play(FadeIn(cache_table_2))
        self.wait()
        self.play(Write(cache_line_text_2))
        self.wait()

        for i in range(4):
            self.play(FlashAround(group_rects[i]))
            cache_line_arrow = Arrow(
                group_rect_labels[i].get_right(),
                cache_table_2[0].get_left(),
                buff=0.2,
                stroke_color=ORANGE,
            )
            self.play(ShowCreation(cache_line_arrow), run_time=0.6)
            new_end = cache_table_2[1].get_left() + LEFT * 0.2
            cache_line_arrow.generate_target()
            cache_line_arrow.target.put_start_and_end_on(
                cache_line_arrow.get_start(), new_end
            )
            self.play(MoveToTarget(cache_line_arrow), run_time=0.6)
            self.play(FadeOut(cache_line_arrow))
        self.wait()
        # 修改bit_table_6和bit_table_4代表以块为单位对地址的重新理解
        bit_table_4_block_index_brace = Brace(bit_table_4[0:2], DOWN)
        bit_table_4_block_index_text = (
            Text("块索引(Block Index)", color=RED_D)
            .scale(0.4)
            .next_to(bit_table_4_block_index_brace, DOWN)
            .shift(RIGHT * 0.2)
        )
        bit_table_4_block_offset_brace = Brace(bit_table_4[2:4], DOWN)
        bit_table_4_block_offset_text = (
            Text("块内偏移(Block Offset)", color=YELLOW_D)
            .scale(0.4)
            .next_to(bit_table_4_block_offset_brace, DOWN)
            .shift(RIGHT * 1)
        )
        bit_table_4[0:2].set_fill(RED_D, opacity=0.8)
        self.wait()
        self.play(ShowCreation(bit_table_4_block_index_brace))
        self.wait()
        self.play(Write(bit_table_4_block_index_text))
        self.wait()
        bit_table_4[2:4].set_fill(YELLOW_D, opacity=0.8)
        self.wait()
        self.play(ShowCreation(bit_table_4_block_offset_brace))
        self.wait()
        self.play(Write(bit_table_4_block_offset_text))
        self.wait()
        bit_table_6[0:2].set_fill(RED_D, opacity=0.8)
        self.wait()
        bit_table_6[2:6].set_fill(YELLOW_D, opacity=0.8)
        self.wait()

        self.play(
            FadeOut(cache_line_text_2),
            FadeOut(cache_table_2),
            FadeOut(group_rects),
            FadeOut(group_rect_labels),
            FadeOut(block_text_2),
            FadeOut(block_line_text_2),
            FadeOut(block_text_1),
            FadeOut(block_line_text_1),
            FadeOut(cache_table),
            FadeOut(cache_line_text_1),
            FadeOut(memory_size_text),
            FadeOut(byte_addressed_text),
            FadeOut(byte_line_text),
            FadeOut(explanation),
            FadeOut(bit_table_6),
            FadeOut(word_addressed_text),
            FadeOut(word_byte_text_1),
            FadeOut(word_line_text),
            FadeOut(explanation_word),
            FadeOut(bit_table_4),
            FadeOut(memory_table),
            FadeOut(bit_table_4_block_index_brace),
            FadeOut(bit_table_4_block_index_text),
            FadeOut(bit_table_4_block_offset_brace),
            FadeOut(bit_table_4_block_offset_text),
        )


class CacheDesign(Scene):
    def construct(self) -> None:
        memory_table = VGroup()
        memory_table_rect = VGroup()
        memory_table_label = VGroup()
        row_labels = VGroup()
        for i in range(16):
            for j in range(4):
                rect = Rectangle(height=0.45, width=0.45)
                rect.shift(RIGHT * j * 0.45 + DOWN * i * 0.45)
                label = Text(str(i * 4 + j), font_size=15, color=BLUE_C).move_to(
                    rect.get_corner(DOWN + RIGHT) + UP * 0.1 + LEFT * 0.1
                )
                memory_table_rect.add(rect)
                memory_table_label.add(label)

            row_label = Text(str(i), font_size=15, color=ORANGE)
            row_label.next_to(memory_table_rect[i * 4], LEFT).shift(DOWN * 0.1)
            row_labels.add(row_label)
        memory_table.add(memory_table_rect, memory_table_label, row_labels)
        memory_table.to_edge(UP, buff=0.3).shift(LEFT * 0.5)

        memory_size_text = Text("内存大小: 64B").to_edge(UP + LEFT).scale(1.2)
        word_byte_text = (
            Text("1字(Word) = 4字节(Byte)", color=RED)
            .scale(0.7)
            .next_to(memory_size_text, DOWN, buff=0.4)
            .align_to(memory_size_text, LEFT)
            .shift(RIGHT * 0.2)
        )
        block_word_text = (
            Text("1块(Block) = 2字(Word)", color=RED)
            .scale(0.7)
            .next_to(word_byte_text, DOWN, buff=0.1)
            .align_to(word_byte_text, LEFT)
        )
        block_word_byte_group = VGroup(word_byte_text, block_word_text)
        block_word_byte_rect = SurroundingRectangle(
            block_word_byte_group, color=YELLOW, stroke_width=2
        )

        colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK, GREY]
        labels = ["0", "1", "2", "3", "4", "5", "6", "7"]
        group_rects = VGroup()
        group_rect_labels = VGroup()
        for index, color in enumerate(colors):
            group_rect = Rectangle(
                height=2 * 0.45,
                width=4 * 0.45,
                fill_opacity=0,
                stroke_color=color,
                stroke_width=4,
            )
            group_rect.move_to(
                memory_table_rect[2 * 4 * index].get_center()
                + DOWN * (3 * 0.45 / 6)
                + RIGHT * (0.68)
            )
            group_rect_label = (
                Text(labels[index], color=color)
                .scale(0.5)
                .next_to(group_rect, RIGHT, buff=0.2)
            )
            group_rects.add(group_rect)
            group_rect_labels.add(group_rect_label)

        simple_table = VGroup()
        simple_table_rect = VGroup()
        simple_table_label = VGroup()
        simple_table.add(simple_table_rect)
        simple_table.add(simple_table_label)
        for i in range(8):
            rect = Rectangle(height=0.8, width=3)
            rect.shift(UP * i * 0.8)
            label = Text(str(i), font_size=15, color=BLUE).scale(2)
            simple_table_rect.add(rect)
            simple_table_label.add(label)
        simple_table_rect.arrange(DOWN, aligned_edge=LEFT, buff=0)
        for i, label in enumerate(simple_table_label):
            label.next_to(simple_table_rect[i], LEFT)

        cache_table = VGroup()
        cache_table_rect = VGroup()
        cache_table_label = VGroup()
        cache_table.add(cache_table_rect)
        cache_table.add(cache_table_label)
        for i in range(4):
            rect = Rectangle(height=1, width=2.5)
            rect.shift(UP * i * 1)
            label = Text(str(i), font_size=20, color=BLUE).scale(2)
            cache_table_rect.add(rect)
            cache_table_label.add(label)
        cache_table_rect.arrange(DOWN, aligned_edge=LEFT, buff=0)
        for i, label in enumerate(cache_table_label):
            label.next_to(cache_table_rect[i], LEFT)

        line_arrow = Arrow(
            cache_table_rect[0].get_right() + RIGHT * 0.1,
            cache_table_rect[0].get_right() + RIGHT * 1.5,
            buff=0.2,
            stroke_color=ORANGE,
        )
        bit_table_8 = VGroup()
        for j in range(2):
            for i in range(4):
                bit_rect = Rectangle(height=0.5, width=0.5)
                bit_label = (
                    Text("", color=YELLOW).scale(0.3).move_to(bit_rect.get_center())
                )
                bit = VGroup(bit_rect, bit_label)

                if i == 0 and j == 0:
                    bit.next_to(line_arrow, RIGHT)
                elif i == 0:
                    bit.next_to(bit_table_8[-4], DOWN, buff=0)
                else:
                    bit.next_to(bit_table_8[-1], RIGHT, buff=0)
                bit_table_8.add(bit)
        bit_table_8.shift(UP * 0.25)

        byte_addressed_text = (
            Text("按字节编址")
            .scale(0.9)
            .next_to(block_word_byte_rect, DOWN, buff=0.2)
            .align_to(block_word_byte_rect, LEFT)
        )
        byte_addressed_explanation = (
            Text("6位<=>64个字节", t2c={"6": BLUE_A, "64": RED_A})
            .next_to(byte_addressed_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(byte_addressed_text, LEFT)
        )

        bit_table_6 = VGroup()
        for i in range(6):
            bit_rect = Rectangle(height=0.6, width=0.6)
            bit_label = Text("", color=YELLOW).scale(0.5).move_to(bit_rect.get_center())
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(byte_addressed_explanation, DOWN, buff=0.1)
            else:
                bit.next_to(bit_table_6[-1], RIGHT, buff=0)
            bit_table_6.add(bit)
        bit_table_6.align_to(byte_addressed_explanation, LEFT)

        byte_offset_brace = Brace(bit_table_6[-3:], DOWN, buff=0.1)
        byte_offset_text = (
            Text("偏移量(Offset)", color=YELLOW_D)
            .scale(0.5)
            .next_to(byte_offset_brace, DOWN, buff=0.1)
        )

        word_addressed_text = (
            Text("按字编址")
            .scale(0.9)
            .next_to(bit_table_6, DOWN, buff=0.5)
            .align_to(bit_table_6, LEFT)
        )
        word_addressed_explanation = (
            Text("4位<=>16个字", t2c={"4": BLUE_A, "16": RED_A, "行": PURPLE_B})
            .next_to(word_addressed_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(word_addressed_text, LEFT)
        )
        bit_table_4 = VGroup()
        for i in range(4):
            bit_rect = Rectangle(height=0.6, width=0.6)
            bit_label = Text("", color=YELLOW).scale(0.5).move_to(bit_rect.get_center())
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(word_addressed_explanation, DOWN, buff=0.1)
            else:
                bit.next_to(bit_table_4[-1], RIGHT, buff=0)
            bit_table_4.add(bit)
        bit_table_4.align_to(word_addressed_explanation, LEFT)

        self.play(FadeIn(memory_table))
        self.wait()
        self.play(Write(memory_size_text))
        self.wait()
        self.play(Write(word_byte_text))
        self.wait()
        self.play(Write(byte_addressed_text))
        self.wait()
        self.play(Write(byte_addressed_explanation))
        self.wait()
        self.play(Write(bit_table_6))
        self.wait()
        self.play(Write(word_addressed_text))
        self.wait()
        self.play(Write(word_addressed_explanation))
        self.wait()
        self.play(Write(bit_table_4))
        self.wait()

        self.play(Write(block_word_text))
        self.wait()
        self.play(ShowCreation(block_word_byte_rect))
        self.wait()
        self.play(ShowCreation(group_rects), Write(group_rect_labels))
        self.wait()
        self.play(FadeOut(memory_table))
        self.wait()
        self.play(
            FadeOut(group_rects),
            FadeOut(group_rect_labels),
        )
        self.wait()
        self.play(ShowCreation(cache_table), run_time=2)
        self.wait()
        self.play(FlashAround(cache_table_rect[0]))
        self.wait()
        self.play(ShowCreation(line_arrow))
        self.wait()
        self.play(ShowCreation(bit_table_8))
        self.wait()

        self.play(
            FadeOut(word_addressed_text),
            FadeOut(word_addressed_explanation),
            FadeOut(bit_table_4),
        )
        self.wait()
        self.play(Indicate(byte_addressed_text))
        self.wait()
        for i in range(8):
            self.play(FlashAround(bit_table_8[i]), run_time=0.5)
        self.wait()
        for i in range(3):
            bit_table_6[-1 - i].set_fill(YELLOW_D, opacity=0.8)
        self.wait()
        self.play(ShowCreation(byte_offset_brace))
        self.wait()
        self.play(Write(byte_offset_text))
        self.wait()
        self.play(
            FadeOut(byte_offset_brace),
            FadeOut(byte_offset_text),
            FadeOut(bit_table_6),
            FadeOut(byte_addressed_text),
            FadeOut(byte_addressed_explanation),
        )
        self.wait()

        word_addressed_text.next_to(block_word_byte_rect, DOWN, buff=0.2).align_to(
            block_word_byte_rect, LEFT
        )
        word_addressed_explanation.next_to(
            word_addressed_text, DOWN, buff=0.1
        ).align_to(word_addressed_text, LEFT)
        bit_table_4.scale(1.5).next_to(
            word_addressed_explanation, DOWN, buff=0.1
        ).align_to(word_addressed_explanation, LEFT)
        word_offset_brace = Brace(bit_table_4[-1], DOWN, buff=0.1)
        word_offset_text = (
            Text("偏移量(Offset)", color=YELLOW_D)
            .scale(0.45)
            .next_to(word_offset_brace, DOWN, buff=0.1)
            .align_to(word_offset_brace, LEFT)
        )
        self.play(Write(word_addressed_text))
        self.wait()
        self.play(Write(word_addressed_explanation))
        self.wait()
        self.play(Write(bit_table_4))
        self.wait()
        self.play(FlashAround(bit_table_8[0:4]))
        self.play(FlashAround(bit_table_8[4:8]))
        self.wait()
        bit_table_4[-1].set_fill(YELLOW_D, opacity=0.8)
        self.wait()
        self.play(ShowCreation(word_offset_brace))
        self.wait()
        self.play(Write(word_offset_text))
        self.wait()
        self.play(
            FadeOut(line_arrow),
            FadeOut(bit_table_8),
        )
        self.wait()

        for i in range(4):
            self.play(FlashAround(cache_table_rect[i]))
        self.wait()

        bit_table_4[1].set_fill(GREEN_C, opacity=0.8)
        bit_table_4[2].set_fill(GREEN_C, opacity=0.8)
        word_index_brace = Brace(bit_table_4[1:3], DOWN, buff=0.1)
        word_index_text = (
            Text("索引(Index)", color=GREEN_C)
            .scale(0.45)
            .next_to(word_index_brace, DOWN, buff=0.1)
            .align_to(word_index_brace, ORIGIN)
        )
        self.play(ShowCreation(word_index_brace))
        self.wait()
        self.play(Write(word_index_text))
        self.wait()

        cache_table.generate_target()
        cache_table.target.shift(RIGHT * 4.5).scale(0.8)
        self.play(MoveToTarget(cache_table))
        self.wait()

        simple_table = VGroup()
        simple_table_rect = VGroup()
        simple_table_label = VGroup()
        simple_table.add(simple_table_rect)
        simple_table.add(simple_table_label)
        for i in range(8):
            rect = Rectangle(height=0.8, width=2)
            rect.shift(UP * i * 0.8)
            label = Text(str(i), font_size=15, color=BLUE).scale(2)
            simple_table_rect.add(rect)
            simple_table_label.add(label)
        simple_table_rect.arrange(DOWN, aligned_edge=LEFT, buff=0)
        simple_table_rect.next_to(cache_table, LEFT, buff=0.3).shift(LEFT * 2)
        for i, label in enumerate(simple_table_label):
            label.next_to(simple_table_rect[i], LEFT)
        self.play(Write(simple_table))
        self.wait()

        table_arrow_0 = Arrow(
            simple_table_rect[0].get_right() + LEFT * 0.1,
            cache_table_rect[0].get_left() + LEFT * 0.15,
            buff=0.2,
            stroke_color=ORANGE,
        )
        table_arrow_1 = Arrow(
            simple_table_rect[1].get_right() + LEFT * 0.1,
            cache_table_rect[0].get_left() + LEFT * 0.15 + DOWN * 0.1,
            buff=0.2,
            stroke_color=ORANGE,
        )
        table_arrow_2 = Arrow(
            simple_table_rect[2].get_right() + LEFT * 0.1,
            cache_table_rect[0].get_left() + LEFT * 0.15 + DOWN * 0.2,
            buff=0.2,
            stroke_color=ORANGE,
        )
        word_tag_brace = Brace(bit_table_4[0], DOWN, buff=0.1)
        word_tag_text = (
            Text("标记(Tag)", color=PURPLE_B)
            .scale(0.45)
            .next_to(word_tag_brace, DOWN, buff=0.1)
            .align_to(word_tag_brace, LEFT)
        )
        self.play(ShowCreation(table_arrow_0))
        self.wait()
        self.play(ShowCreation(table_arrow_1))
        self.wait()
        bit_table_4[0].set_fill(PURPLE_B, opacity=0.8)
        self.play(ShowCreation(word_tag_brace))
        self.wait()
        self.play(Write(word_tag_text))
        self.wait()

        self.play(Indicate(bit_table_4[0]))
        self.wait()
        self.play(ShowCreation(table_arrow_2))
        self.wait()

        mapping_title = (
            Text("映射策略", color=ORANGE)
            .next_to(bit_table_4, DOWN, buff=0.4)
            .align_to(bit_table_4, LEFT)
            .shift(DOWN * 0.8)
        )
        table_arrow_group_1 = VGroup(table_arrow_0, table_arrow_1, table_arrow_2)
        direct_mapping_text = (
            Text("直接映射(Direct-mapped)")
            .scale(0.75)
            .next_to(mapping_title, DOWN, buff=0.2)
            .align_to(mapping_title, LEFT)
        )
        table_arrow_group_2 = VGroup()
        direct_color_set = [RED_B, BLUE_B, GREEN_B, YELLOW_B]
        for i in range(8):
            j = i
            if i > 3:
                j = i - 4
            arrow = Arrow(
                simple_table_rect[i].get_right() + LEFT * 0.1,
                cache_table_rect[j].get_left() + LEFT * 0.15,
                buff=0.2,
                stroke_color=direct_color_set[j],
            )
            table_arrow_group_2.add(arrow)
        direct_mapping_advantage = (
            Text("优点: 硬件设计容易, 查询速度快", color=GREEN_B)
            .scale(0.6)
            .next_to(cache_table, UP, buff=0.2)
            .align_to(cache_table, LEFT)
            .shift(UP * 0.5 + LEFT * 0.4)
        )
        direct_mapping_disadvantage = (
            Text("缺点: 冲突严重", color=RED_C)
            .scale(0.7)
            .next_to(cache_table, DOWN, buff=0.2)
            .align_to(cache_table, LEFT)
            .shift(DOWN * 0.5)
        )

        self.play(ReplacementTransform(table_arrow_group_1, mapping_title))
        self.wait()
        self.play(Write(direct_mapping_text))
        self.wait()
        for i in range(8):
            self.play(ShowCreation(table_arrow_group_2[i]))
        self.wait()
        self.play(Indicate(table_arrow_group_2[0]), run_time=0.5)
        self.play(Indicate(table_arrow_group_2[4]), run_time=0.5)
        self.wait()
        self.play(Write(direct_mapping_advantage))
        self.wait()
        self.play(Write(direct_mapping_disadvantage))
        self.wait()
        self.play(
            FadeOut(direct_mapping_text),
            FadeOut(table_arrow_group_2),
            FadeOut(direct_mapping_advantage),
            FadeOut(direct_mapping_disadvantage),
        )
        self.wait()

        fully_associative_text = (
            Text("全相联映射(Fully associative)")
            .scale(0.75)
            .next_to(mapping_title, DOWN, buff=0.2)
            .align_to(mapping_title, LEFT)
        )
        table_arrow_group_3 = VGroup()
        for i in range(4):
            for j in range(8):
                arrow = Arrow(
                    simple_table_rect[j].get_right() + LEFT * 0.1,
                    cache_table_rect[i].get_left() + LEFT * 0.15,
                    buff=0.2,
                    stroke_color=direct_color_set[i],
                    stroke_width=2,
                )
                table_arrow_group_3.add(arrow)
        fully_associative_tag_brace = Brace(bit_table_4[0:3], DOWN, buff=0.1)
        fully_associative_tag_text = (
            Text("标记(Tag)", color=PURPLE_B)
            .scale(0.45)
            .next_to(fully_associative_tag_brace, DOWN, buff=0.1)
            .align_to(fully_associative_tag_brace, ORIGIN)
        )
        fully_associative_advantage = (
            Text("优点: 冲突少", color=GREEN_B)
            .scale(0.7)
            .next_to(cache_table, UP, buff=0.2)
            .align_to(cache_table, LEFT)
            .shift(UP * 0.5)
        )
        fully_associative_disadvantage = (
            Text("缺点: 查询速度慢, 硬件设计复杂", color=RED_C)
            .scale(0.6)
            .next_to(cache_table, DOWN, buff=0.2)
            .align_to(cache_table, LEFT)
            .shift(DOWN * 0.5 + LEFT * 0.4)
        )
        self.play(Write(fully_associative_text))
        self.wait()
        # 首先应该展示0、8、16、24，再展示1、9、17、25，直到7、15、23、31
        for i in range(8):
            for j in range(4):
                if i == 0:
                    self.play(ShowCreation(table_arrow_group_3[i + j * 8]))
                else:
                    self.play(
                        ShowCreation(table_arrow_group_3[i + j * 8]), run_time=0.1
                    )
        self.wait()
        bit_table_4[1:3].set_fill(PURPLE_B, opacity=0.8)
        self.play(
            FadeOut(word_index_brace),
            FadeOut(word_index_text),
            FadeOut(word_tag_brace),
            FadeOut(word_tag_text),
        )
        self.wait()
        self.play(ShowCreation(fully_associative_tag_brace))
        self.wait()
        self.play(Write(fully_associative_tag_text))
        self.wait()
        for i in range(8):
            self.play(Indicate(table_arrow_group_3[i]), run_time=0.5)
        self.wait()
        self.play(Write(fully_associative_advantage))
        self.wait()
        self.play(Write(fully_associative_disadvantage))
        self.wait()
        self.play(
            FadeOut(fully_associative_text),
            FadeOut(fully_associative_advantage),
            FadeOut(fully_associative_disadvantage),
            FadeOut(table_arrow_group_3),
        )

        set_associative_text = (
            Text("组相联映射(Set-associative)")
            .scale(0.75)
            .next_to(mapping_title, DOWN, buff=0.2)
            .align_to(mapping_title, LEFT)
        )
        set_1_block_text = (
            Text("组中有一个块: 1路组相联", color=GREEN_B)
            .scale(0.75)
            .next_to(set_associative_text, DOWN, buff=0.2)
            .align_to(set_associative_text, LEFT)
        )
        set_2_block_text = (
            Text("组中有两个块: 2路组相联", color=GREEN_B)
            .scale(0.75)
            .next_to(set_associative_text, DOWN, buff=0.2)
            .align_to(set_associative_text, LEFT)
        )
        cache_colors = [TEAL_B, LIGHT_PINK]
        cache_labels = ["0", "1"]
        cache_group_rects = VGroup()
        cache_group_rect_labels = VGroup()
        for index, color in enumerate(cache_colors):
            cache_group_rect = Rectangle(
                height=2 * 0.8,
                width=2,
                fill_opacity=0,
                stroke_color=color,
                stroke_width=3,
            )
            cache_group_rect.move_to(
                cache_table_rect[2 * 1 * index].get_center()
                + DOWN * (3 * 0.8 / 6)
                + RIGHT * 0
            )
            cache_group_rect_label = (
                Text(cache_labels[index], color=color)
                .scale(0.8)
                .next_to(cache_group_rect, RIGHT, buff=0.2)
            )
            cache_group_rects.add(cache_group_rect)
            cache_group_rect_labels.add(cache_group_rect_label)

        table_arrow_group_4 = VGroup()
        # 内存的每一行指向组内的每一个块
        for i in range(8):
            for j in range(2):
                if i % 2 == 0:
                    arrow = Arrow(
                        simple_table_rect[i].get_right() + LEFT * 0.1,
                        cache_table_rect[j].get_left() + LEFT * 0.15,
                        buff=0.2,
                        stroke_color=cache_colors[0],
                        stroke_width=2,
                    )
                else:
                    arrow = Arrow(
                        simple_table_rect[i].get_right() + LEFT * 0.1,
                        cache_table_rect[j + 2].get_left() + LEFT * 0.15,
                        buff=0.2,
                        stroke_color=cache_colors[1],
                        stroke_width=2,
                    )
                table_arrow_group_4.add(arrow)
        set_associative_feature = (
            Text(
                """
                 折衷: 
                   冲突、查询速度、硬件设计复杂度
                """,
                color=ORANGE,
            )
            .scale(0.6)
            .next_to(cache_table, UP, buff=0.2)
            .align_to(cache_table, LEFT)
            .shift(UP * 0.5 + LEFT * 0.8)
        )

        self.play(Write(set_associative_text))
        self.wait()
        self.play(Write(set_1_block_text))
        self.wait()
        for i in range(4):
            self.play(FlashAround(cache_table_rect[i]))
        self.wait()
        self.play(ReplacementTransform(set_1_block_text, set_2_block_text))
        self.wait()
        self.play(ShowCreation(cache_group_rects), Write(cache_group_rect_labels))
        self.wait()
        self.play(
            FadeOut(fully_associative_tag_brace), FadeOut(fully_associative_tag_text)
        )
        self.wait()
        bit_table_4[2].set_fill(GREEN_C, opacity=0.8)
        set_associative_index_brace = Brace(bit_table_4[2], DOWN, buff=0.1)
        set_associative_index_text = (
            Text("索引(Index)", color=GREEN_C)
            .scale(0.45)
            .next_to(set_associative_index_brace, DOWN, buff=0.1)
            .align_to(set_associative_index_brace, LEFT)
            .shift(LEFT * 0.24)
        )
        set_associative_tag_brace = Brace(bit_table_4[0:2], DOWN, buff=0.1)
        set_associative_tag_text = (
            Text("标记(Tag)", color=PURPLE_B)
            .scale(0.45)
            .next_to(set_associative_tag_brace, DOWN, buff=0.1)
            .align_to(set_associative_tag_brace, ORIGIN)
        )
        self.play(ShowCreation(set_associative_index_brace))
        self.wait()
        self.play(Write(set_associative_index_text))
        self.wait()
        self.play(ShowCreation(set_associative_tag_brace))
        self.wait()
        self.play(Write(set_associative_tag_text))
        self.wait()
        for i in range(16):
            self.play(ShowCreation(table_arrow_group_4[i]))
        self.wait()
        # 高亮指向第一个缓存槽的四条箭头
        for i in range(4):
            self.play(Indicate(table_arrow_group_4[i * 4]), run_time=0.5)
        self.wait()
        self.play(Write(set_associative_feature))
        self.wait()

        self.clear()


class CacheMapping(Scene):
    def construct(self) -> None:
        divider_left = Line(UP * 2.8, DOWN * 2.5).shift(LEFT * 2.5)
        divider_right = Line(UP * 2.8, DOWN * 2.5).shift(RIGHT * 2.5)
        divider = VGroup(divider_left, divider_right)
        mapping_title = Text("三种映射策略", color=BLUE).to_edge(UP).scale(1.5)
        fully_associative_text = (
            Text("全相联映射(Fully associative)")
            .scale(0.7)
            .next_to(mapping_title, DOWN, buff=0.3)
            .align_to(mapping_title, LEFT)
        )
        direct_mapping_text = (
            Text("直接映射(Direct-mapped)")
            .scale(0.7)
            .next_to(fully_associative_text, LEFT, buff=0.2)
            .shift(LEFT * 0.5)
        )
        set_associative_text = (
            Text("组相联映射(Set-associative)")
            .scale(0.7)
            .next_to(fully_associative_text, RIGHT, buff=0.2)
            .shift(RIGHT * 0.2)
        )
        fully_simple_table = VGroup()
        for i in range(8):
            rect = Rectangle(height=0.8, width=2)
            rect.shift(UP * i * 0.8)
            fully_simple_table.add(rect)
        fully_simple_table.arrange(DOWN, aligned_edge=LEFT, buff=0)
        fully_simple_table.scale(0.5).next_to(
            fully_associative_text, DOWN, buff=0.2
        ).shift(LEFT * 1.5)
        fully_cache_table = VGroup()
        for i in range(4):
            rect = Rectangle(height=0.5, width=3)
            rect.shift(UP * i * 0.5)
            fully_cache_table.add(rect)
        fully_cache_table.arrange(DOWN, aligned_edge=LEFT, buff=0)
        fully_cache_table.scale(0.6).next_to(fully_simple_table, RIGHT, buff=0.3).shift(
            RIGHT * 0.8
        )
        direct_simple_table = (
            fully_simple_table.copy()
            .next_to(direct_mapping_text, DOWN, buff=0.2)
            .shift(LEFT * 1.5)
        )
        direct_cache_table = (
            fully_cache_table.copy()
            .next_to(direct_simple_table, RIGHT, buff=0.3)
            .shift(RIGHT * 0.8)
        )
        set_simple_table = (
            fully_simple_table.copy()
            .next_to(set_associative_text, DOWN, buff=0.2)
            .shift(LEFT * 1.5)
        )
        set_cache_table = (
            fully_cache_table.copy()
            .next_to(set_simple_table, RIGHT, buff=0.3)
            .shift(RIGHT * 0.8)
        )
        direct_arrow_group = VGroup()
        direct_color_set = [RED_B, BLUE_B, GREEN_B, YELLOW_B]
        for i in range(8):
            j = i
            if i > 3:
                j = i - 4
            arrow = Arrow(
                direct_simple_table[i].get_right(),
                direct_cache_table[j].get_left(),
                buff=0.05,
                stroke_color=direct_color_set[j],
                stroke_width=2,
            )
            direct_arrow_group.add(arrow)
        fully_arrow_group = VGroup()
        for i in range(4):
            for j in range(8):
                arrow = Arrow(
                    fully_simple_table[j].get_right(),
                    fully_cache_table[i].get_left(),
                    buff=0.05,
                    stroke_color=direct_color_set[i],
                    stroke_width=2,
                )
                fully_arrow_group.add(arrow)
        set_arrow_group = VGroup()
        cache_colors = [TEAL_B, LIGHT_PINK]
        for i in range(8):
            for j in range(2):
                if i % 2 == 0:
                    arrow = Arrow(
                        set_simple_table[i].get_right(),
                        set_cache_table[j].get_left(),
                        buff=0.05,
                        stroke_color=cache_colors[0],
                        stroke_width=2,
                    )
                else:
                    arrow = Arrow(
                        set_simple_table[i].get_right(),
                        set_cache_table[j + 2].get_left(),
                        buff=0.05,
                        stroke_color=cache_colors[1],
                        stroke_width=2,
                    )
                set_arrow_group.add(arrow)
        direct_bit_table_4 = VGroup()
        for i in range(4):
            bit_rect = Rectangle(height=0.6, width=0.6)
            bit_label = Text("", color=YELLOW).scale(0.6).move_to(bit_rect.get_center())
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(direct_simple_table, DOWN, buff=0.1)
            else:
                bit.next_to(direct_bit_table_4[-1], RIGHT, buff=0)
            direct_bit_table_4.add(bit)
        direct_bit_table_4.align_to(direct_simple_table, ORIGIN).shift(
            DOWN * 0.15 + RIGHT * 0.4
        )
        fully_bit_table_4 = (
            direct_bit_table_4.copy()
            .next_to(fully_simple_table, DOWN, buff=0.1)
            .align_to(fully_simple_table, LEFT)
            .shift(DOWN * 0.15 + RIGHT * 0.5)
        )
        set_bit_table_4 = (
            direct_bit_table_4.copy()
            .next_to(set_simple_table, DOWN, buff=0.1)
            .align_to(set_simple_table, LEFT)
            .shift(DOWN * 0.15 + RIGHT * 0.5)
        )
        direct_tag_brace = Brace(direct_bit_table_4[0], DOWN, buff=0.1)
        direct_bit_table_4[0].set_fill(PURPLE_B, opacity=0.8)
        direct_tag_text = (
            Text("标记", color=PURPLE_B)
            .scale(0.45)
            .next_to(direct_tag_brace, DOWN, buff=0.1)
            .align_to(direct_tag_brace, ORIGIN)
        )
        fully_tag_brace = Brace(fully_bit_table_4[0:3], DOWN, buff=0.1)
        fully_bit_table_4[0:3].set_fill(PURPLE_B, opacity=0.8)
        fully_tag_text = (
            Text("标记", color=PURPLE_B)
            .scale(0.45)
            .next_to(fully_tag_brace, DOWN, buff=0.1)
            .align_to(fully_tag_brace, ORIGIN)
        )
        set_tag_brace = Brace(set_bit_table_4[0:2], DOWN, buff=0.1)
        set_bit_table_4[0:2].set_fill(PURPLE_B, opacity=0.8)
        set_tag_text = (
            Text("标记", color=PURPLE_B)
            .scale(0.45)
            .next_to(set_tag_brace, DOWN, buff=0.1)
            .align_to(set_tag_brace, ORIGIN)
        )
        direct_index_brace = Brace(direct_bit_table_4[1:3], DOWN, buff=0.1)
        direct_bit_table_4[1:3].set_fill(GREEN_C, opacity=0.8)
        direct_index_text = (
            Text("索引", color=GREEN_C)
            .scale(0.45)
            .next_to(direct_index_brace, DOWN, buff=0.1)
            .align_to(direct_index_brace, ORIGIN)
        )
        set_index_brace = Brace(set_bit_table_4[2], DOWN, buff=0.1)
        set_bit_table_4[2].set_fill(GREEN_C, opacity=0.8)
        set_index_text = (
            Text("索引", color=GREEN_C)
            .scale(0.45)
            .next_to(set_index_brace, DOWN, buff=0.1)
            .align_to(set_index_brace, ORIGIN)
        )
        direct_offset_brace = Brace(direct_bit_table_4[-1], DOWN, buff=0.1)
        direct_bit_table_4[-1].set_fill(YELLOW_D, opacity=0.8)
        direct_offset_text = (
            Text("偏移量", color=YELLOW_D)
            .scale(0.45)
            .next_to(direct_offset_brace, DOWN, buff=0.1)
            .align_to(direct_offset_brace, ORIGIN)
        )
        fully_offset_brace = Brace(fully_bit_table_4[-1], DOWN, buff=0.1)
        fully_bit_table_4[-1].set_fill(YELLOW_D, opacity=0.8)
        fully_offset_text = (
            Text("偏移量", color=YELLOW_D)
            .scale(0.45)
            .next_to(fully_offset_brace, DOWN, buff=0.1)
            .align_to(fully_offset_brace, ORIGIN)
        )
        set_offset_brace = Brace(set_bit_table_4[-1], DOWN, buff=0.1)
        set_bit_table_4[-1].set_fill(YELLOW_D, opacity=0.8)
        set_offset_text = (
            Text("偏移量", color=YELLOW_D)
            .scale(0.45)
            .next_to(set_offset_brace, DOWN, buff=0.1)
            .align_to(set_offset_brace, ORIGIN)
        )

        direct_mapping_advantage = (
            Text("优点: 硬件设计容易; 查询速度快", color=GREEN_B)
            .scale(0.6)
            .next_to(direct_simple_table, DOWN, buff=0.2)
            .align_to(direct_simple_table, LEFT)
            .shift(DOWN * 1.5)
        )
        direct_mapping_disadvantage = (
            Text("缺点: 冲突严重", color=RED_C)
            .scale(0.6)
            .next_to(direct_mapping_advantage, DOWN, buff=0.1)
            .align_to(direct_mapping_advantage, LEFT)
        )
        fully_associative_advantage = (
            Text("优点: 冲突少", color=GREEN_B)
            .scale(0.6)
            .next_to(fully_simple_table, DOWN, buff=0.2)
            .align_to(fully_simple_table, LEFT)
            .shift(DOWN * 1.5)
        )
        fully_associative_disadvantage = (
            Text("缺点: 硬件设计复杂; 查询速度慢", color=RED_C)
            .scale(0.6)
            .next_to(fully_associative_advantage, DOWN, buff=0.1)
            .align_to(fully_associative_advantage, LEFT)
        )
        set_associative_feature = (
            Text("折衷选择", color=ORANGE)
            .scale(1)
            .next_to(set_simple_table, DOWN, buff=0.2)
            .align_to(set_simple_table, LEFT)
            .shift(DOWN * 1.5 + RIGHT * 0.8)
        )

        self.play(Write(mapping_title))
        self.wait()
        self.play(ShowCreation(divider))
        self.wait()

        self.play(Write(direct_mapping_text))
        self.wait()
        self.play(
            FadeIn(direct_simple_table),
            FadeIn(direct_cache_table),
        )
        self.wait()
        self.play(ShowCreation(direct_arrow_group))
        self.wait()
        self.play(
            Write(direct_bit_table_4),
            ShowCreation(direct_tag_brace),
            Write(direct_tag_text),
            ShowCreation(direct_index_brace),
            Write(direct_index_text),
            ShowCreation(direct_offset_brace),
            Write(direct_offset_text),
        )
        self.wait()
        self.play(Write(direct_mapping_advantage), Write(direct_mapping_disadvantage))
        self.wait()

        self.play(Write(fully_associative_text))
        self.wait()
        self.play(
            FadeIn(fully_simple_table),
            FadeIn(fully_cache_table),
        )
        self.play(ShowCreation(fully_arrow_group))
        self.wait()
        self.play(
            Write(fully_bit_table_4),
            ShowCreation(fully_tag_brace),
            Write(fully_tag_text),
            ShowCreation(fully_offset_brace),
            Write(fully_offset_text),
        )
        self.wait()
        self.play(
            Write(fully_associative_advantage),
            Write(fully_associative_disadvantage),
        )
        self.wait()

        self.play(Write(set_associative_text))
        self.wait()
        self.play(
            FadeIn(set_simple_table),
            FadeIn(set_cache_table),
        )
        self.wait()
        self.play(ShowCreation(set_arrow_group))
        self.wait()
        self.play(
            Write(set_bit_table_4),
            ShowCreation(set_tag_brace),
            Write(set_tag_text),
            ShowCreation(set_index_brace),
            Write(set_index_text),
            ShowCreation(set_offset_brace),
            Write(set_offset_text),
        )
        self.wait()
        self.play(Write(set_associative_feature))
        self.wait()
        # self.clear()


class CacheStructure(Scene):
    def construct(self) -> None:
        memory_title = (
            Text("内存(Memory)", color=MAROON_B)
            .scale(1.2)
            .to_edge(UP + LEFT)
            .shift(RIGHT * 1.2)
        )
        cache_title = (
            Text("缓存(Cache)", color=MAROON_B)
            .scale(1.2)
            .to_edge(UP + RIGHT)
            .shift(LEFT * 1.2)
        )
        divider = Line(UP * 2.8, DOWN * 3)

        memory_address_title = (
            Text("地址", color=BLUE)
            .scale(0.8)
            .next_to(memory_title, DOWN, buff=0.4)
            .shift(LEFT)
        )
        memory_storage_title = (
            Text("存储空间", color=WHITE)
            .scale(0.8)
            .next_to(memory_address_title, RIGHT)
            .shift(RIGHT * 0.5)
        )

        simple_table = VGroup()
        simple_table_rect = VGroup()
        simple_table_label = VGroup()
        simple_table.add(simple_table_rect)
        simple_table.add(simple_table_label)
        for i in range(8):
            rect = Rectangle(height=0.8, width=2)
            rect.shift(UP * i * 0.8)
            label = Text(str(i), font_size=15, color=BLUE).scale(2)
            simple_table_rect.add(rect)
            simple_table_label.add(label)
        simple_table_rect.arrange(DOWN, aligned_edge=LEFT, buff=0)
        simple_table_rect.scale(0.5).next_to(memory_storage_title, DOWN, buff=0.3)
        for i, label in enumerate(simple_table_label):
            label.next_to(simple_table_rect[i], LEFT).align_to(
                memory_address_title, LEFT
            ).shift(RIGHT * 0.2)

        cache_storage_title = (
            Text("存储空间", color=WHITE)
            .scale(0.8)
            .next_to(cache_title, DOWN, buff=0.4)
            .shift(RIGHT * 0.5)
        )
        cache_control_title = (
            Text("控制信息", color=YELLOW_C)
            .scale(0.8)
            .next_to(cache_storage_title, LEFT)
            .shift(LEFT * 0.75)
        )
        cache_table = VGroup()
        for i in range(4):
            rect = Rectangle(height=0.5, width=3)
            rect.shift(UP * i * 0.5)
            label = Text(str(i), font_size=15, color=YELLOW).next_to(rect, LEFT)
            cache_table.add(rect)
        cache_table.arrange(DOWN, aligned_edge=LEFT, buff=0)
        cache_table.next_to(cache_storage_title, DOWN, buff=0.3)

        control_table = VGroup()
        for i in range(4):
            valid_bit_rect = Rectangle(
                height=0.5, width=0.3, fill_color=TEAL_B, fill_opacity=0.6
            )
            dirty_bit_rect = Rectangle(
                height=0.5, width=0.3, fill_color=RED_B, fill_opacity=0.6
            )
            tag_bit_rect = Rectangle(
                height=0.5, width=1.4, fill_color=PURPLE_B, fill_opacity=0.5
            )
            control_rect_group = VGroup(
                valid_bit_rect, dirty_bit_rect, tag_bit_rect
            ).arrange(RIGHT, buff=0)
            valid_bit_label = (
                Text("V", color=WHITE).scale(0.4).move_to(valid_bit_rect.get_center())
            )
            dirty_bit_label = (
                Text("D", color=WHITE).scale(0.4).move_to(dirty_bit_rect.get_center())
            )
            tag_bit_label = (
                Text("Tag", color=WHITE).scale(0.4).move_to(tag_bit_rect.get_center())
            )
            control_label_group = VGroup(
                valid_bit_label, tag_bit_label, dirty_bit_label
            )
            control_group = VGroup(control_rect_group, control_label_group)
            control_table.add(control_group)
        control_table.arrange(DOWN, aligned_edge=LEFT, buff=0)
        control_table.next_to(cache_control_title, DOWN, buff=0.3)

        slot_title = (
            Text("槽(slot)", color=ORANGE)
            .scale(0.6)
            .next_to(cache_table[0], RIGHT, buff=0.15)
        )
        slot_0 = VGroup(cache_table[0], control_table[0])
        slot_flash_rect = SurroundingRectangle(slot_0, color=ORANGE, stroke_width=2)

        self.play(Write(memory_title), Write(cache_title))
        self.wait()
        self.play(ShowCreation(divider))
        self.wait(2)

        self.play(Write(memory_storage_title))
        self.play(FadeIn(simple_table_rect))
        self.wait()
        self.play(Write(memory_address_title))
        self.wait()
        for label in simple_table_label:
            self.play(Write(label, run_time=0.3))
        self.wait()

        self.play(Write(cache_storage_title))
        self.wait()
        self.play(FadeIn(cache_table))
        self.wait()
        self.play(Write(cache_control_title))
        self.wait()
        self.play(FadeIn(control_table))
        self.wait()
        self.play(ShowCreation(slot_flash_rect))
        self.wait()
        self.play(Write(slot_title))
        self.wait()

        rect_height = 0.6
        memory_long_rect = Rectangle(
            width=4, height=rect_height, fill_color=WHITE, fill_opacity=1
        )
        memory_long_rect.next_to(simple_table, DOWN, buff=0.3).align_to(
            simple_table, LEFT
        )
        memory_cache_long_rect = memory_long_rect.copy()
        memory_cache_long_rect.next_to(memory_long_rect, DOWN, buff=0.2)

        memory_address_structure_title = (
            Text("块为单位对地址的理解: ", color=ORANGE)
            .scale(0.4)
            .next_to(memory_long_rect, LEFT, buff=0.2)
        )

        memory_cache_structure_title = (
            Text("Cache对地址重新理解: ", color=ORANGE)
            .scale(0.4)
            .next_to(memory_cache_long_rect, LEFT, buff=0.2)
        )

        memory_line_0 = (
            Line(UP * rect_height / 2, DOWN * rect_height / 2)
            .next_to(memory_long_rect.get_left(), RIGHT, buff=3)
            .set_color(BLACK)
        )

        memory_line1 = (
            Line(UP * rect_height / 2, DOWN * rect_height / 2)
            .next_to(memory_cache_long_rect.get_left(), RIGHT, buff=2)
            .set_color(BLACK)
        )
        memory_line2 = (
            Line(UP * rect_height / 2, DOWN * rect_height / 2)
            .next_to(memory_cache_long_rect.get_right(), LEFT, buff=1)
            .set_color(BLACK)
        )

        memory_rect01 = Rectangle(
            width=3, height=rect_height, fill_color=RED_D, fill_opacity=0.8
        )
        memory_rect02 = Rectangle(
            width=1, height=rect_height, fill_color=YELLOW_D, fill_opacity=0.8
        )

        memory_rect1 = Rectangle(
            width=2, height=rect_height, fill_color=PURPLE_B, fill_opacity=0.8
        )
        memory_rect2 = Rectangle(
            width=1, height=rect_height, fill_color=GREEN_C, fill_opacity=0.8
        )
        memory_rect3 = Rectangle(
            width=1, height=rect_height, fill_color=YELLOW_D, fill_opacity=0.8
        )

        memory_rect01.next_to(memory_long_rect.get_left(), RIGHT, buff=0).align_to(
            memory_long_rect, UP
        )
        memory_rect02.next_to(memory_rect01, RIGHT, buff=0).align_to(
            memory_long_rect, UP
        )

        memory_rect1.next_to(memory_cache_long_rect.get_left(), RIGHT, buff=0).align_to(
            memory_cache_long_rect, UP
        )
        memory_rect2.next_to(memory_rect1, RIGHT, buff=0).align_to(
            memory_cache_long_rect, UP
        )
        memory_rect3.next_to(memory_rect2, RIGHT, buff=0).align_to(
            memory_cache_long_rect, UP
        )

        memory_rect01_label = (
            Text("块索引", color=BLACK).scale(0.45).move_to(memory_rect01.get_center())
        )
        memory_rect02_label = (
            Text("块内偏移", color=BLACK).scale(0.45).move_to(memory_rect02.get_center())
        )
        memory_rect1_label = (
            Text("标记", color=BLACK).scale(0.45).move_to(memory_rect1.get_center())
        )
        memory_rect2_label = (
            Text("组索引", color=BLACK).scale(0.45).move_to(memory_rect2.get_center())
        )
        memory_rect3_label = (
            Text("偏移", color=BLACK).scale(0.45).move_to(memory_rect3.get_center())
        )

        memory_cache_long_rect_tag_brace = Brace(memory_rect1, DOWN, buff=0.1)

        mem2cache_tag_arrow = CurvedArrow(
            memory_cache_long_rect_tag_brace.get_bottom() + DOWN * 0.1,
            control_table.get_bottom() + DOWN * 0.1,
            angle=TAU / 4,
            stroke_width=2,
        )

        total_capacity_text = (
            Text(
                "总容量 = (有效位+标志位+TAG+块容量) * 行数",
                color=WHITE,
                t2c={"有效位": TEAL_B, "标志位": RED_B, "TAG": PURPLE_B},
            )
            .scale(0.6)
            .next_to(control_table, DOWN, buff=0.2)
            .align_to(control_table, LEFT)
            .shift(DOWN * 1 + LEFT * 0.2)
        )
        storage_capacity_text = (
            Text("存储容量 = 块容量 * 行数", color=WHITE)
            .scale(0.6)
            .next_to(total_capacity_text, DOWN, buff=0.4)
            .align_to(total_capacity_text, LEFT)
        )
        cache_address_structure_title = (
            Text("Cache地址: ", color=ORANGE)
            .scale(0.5)
            .next_to(storage_capacity_text, DOWN, buff=0.2)
            .align_to(storage_capacity_text, LEFT)
            .shift(DOWN * 0.2)
        )
        cache_long_rect = Rectangle(
            width=2.5, height=rect_height, fill_color=WHITE, fill_opacity=1
        )
        cache_long_rect.next_to(cache_address_structure_title, RIGHT, buff=0.2)
        cache_line = (
            Line(UP * rect_height / 2, DOWN * rect_height / 2)
            .next_to(cache_long_rect.get_left(), RIGHT, buff=1.5)
            .set_color(BLACK)
        )
        cache_rect_1 = Rectangle(
            width=1.5, height=rect_height, fill_color=PINK, fill_opacity=0.8
        )
        cache_rect_2 = Rectangle(
            width=1, height=rect_height, fill_color=YELLOW_D, fill_opacity=0.8
        )
        cache_rect_1.next_to(cache_long_rect.get_left(), RIGHT, buff=0).align_to(
            cache_long_rect, UP
        )
        cache_rect_2.next_to(cache_rect_1, RIGHT, buff=0).align_to(cache_long_rect, UP)
        cache_rect1_label = (
            Text("行索引", color=BLACK).scale(0.45).move_to(cache_rect_1.get_center())
        )
        cache_rect2_label = (
            Text("行内偏移", color=BLACK).scale(0.45).move_to(cache_rect_2.get_center())
        )

        mem2cache_arrow = CurvedDoubleArrow(
            memory_long_rect.get_right() + LEFT*0.2+UP*0.1,
            cache_address_structure_title.get_left() + LEFT * 0.1,
            angle=0,
        ).scale(0.6)

        storage_extra_text = (
            Tex(r"= 2^{\text{bits}}", color=WHITE)
            .scale(0.8)
            .next_to(storage_capacity_text, RIGHT, buff=0.2)
            .shift(UP*0.05)
        )

        cache_rect_brace = Brace(cache_long_rect, DOWN, buff=0.18)

        cache_address2storage_arrow = CurvedArrow(
            storage_extra_text.get_right(),
            cache_rect_brace.get_bottom(),
            angle= -TAU / 3,
            stroke_width=3,
        )

        block_example = (
            Text("2W", color=ORANGE)
            .scale(0.6)
            .next_to(storage_capacity_text, UP, buff=0.1)
            .shift(RIGHT*0.2)
        )
        line_example = (
            Text("4", color=ORANGE)
            .scale(0.6)
            .next_to(block_example, RIGHT, buff=0.2)
            .shift(RIGHT*0.7)
        )
        bit_example = (
            Text("3", color=ORANGE)
            .scale(0.6)
            .next_to(storage_extra_text, RIGHT, buff=0.2)
        )
        line_index_example = (
            Text("2", color=ORANGE)
            .scale(0.6)
            .next_to(cache_rect_1, DOWN, buff=0.06)
        )
        offset_example = (
            Text("1", color=ORANGE)
            .scale(0.6)
            .next_to(cache_rect_2, DOWN, buff=0.06)
        )


        self.play(Write(memory_address_structure_title))
        self.wait()
        self.play(ShowCreation(memory_long_rect))
        self.wait()

        self.play(GrowFromCenter(memory_line_0))
        self.wait()
        self.play(ShowCreation(memory_rect01), ShowCreation(memory_rect02))
        self.wait()
        self.play(Write(memory_rect01_label), Write(memory_rect02_label))
        self.wait()

        self.play(Write(memory_cache_structure_title))
        self.wait()
        self.play(ShowCreation(memory_cache_long_rect))
        self.wait()
        self.play(GrowFromCenter(memory_line1), GrowFromCenter(memory_line2))
        self.wait()
        self.play(
            ShowCreation(memory_rect1),
            ShowCreation(memory_rect2),
            ShowCreation(memory_rect3),
        )
        self.wait()
        self.play(
            Write(memory_rect1_label),
            Write(memory_rect2_label),
            Write(memory_rect3_label),
        )
        self.wait()

        self.play(ShowCreation(memory_cache_long_rect_tag_brace))
        self.wait()
        self.play(ShowCreation(mem2cache_tag_arrow))
        self.wait()
        self.play(
            FadeOut(memory_cache_long_rect_tag_brace), FadeOut(mem2cache_tag_arrow)
        )

        self.play(Write(total_capacity_text))
        self.wait()
        self.play(Write(storage_capacity_text))
        self.wait()

        self.play(Write(cache_address_structure_title))
        self.wait()
        self.play(ShowCreation(cache_long_rect))
        self.wait()
        self.play(GrowFromCenter(cache_line))
        self.wait()
        self.play(ShowCreation(cache_rect_1), ShowCreation(cache_rect_2))
        self.wait()
        self.play(Write(cache_rect1_label), Write(cache_rect2_label))
        self.wait()
        self.play(ShowCreation(mem2cache_arrow))
        self.wait()
        self.play(Write(storage_extra_text))
        self.wait()
        self.play(ShowCreation(cache_address2storage_arrow))
        self.wait()
        self.play(ShowCreation(cache_rect_brace))
        self.wait()
        self.play(Write(block_example))
        self.wait()
        self.play(Write(line_example))
        self.wait()
        self.play(Write(bit_example))
        self.wait()
        self.play(Write(line_index_example))
        self.wait()
        self.play(Write(offset_example))
        self.wait()


class CacheCover(Scene):
    def construct(self) -> None:
        title = (
            Text("理解Cache", color=YELLOW)
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
        self.add(trick)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = f"manimgl {module_name} CacheCover"
    os.system(command)
