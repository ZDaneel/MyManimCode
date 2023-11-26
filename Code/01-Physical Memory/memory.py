from manimlib import *
import numpy as np


class Introduction(Scene):
    def construct(self):
        # 创建标题
        title = Text("内存(Memory)", color=MAROON_B).scale(1.5)
        title.to_edge(UP + LEFT)
        self.play(Write(title), run_time=2)
        self.wait()

        real_mem_text = Text(
            "装机视角: 内存条", color=BLUE, t2w={"内存条": BOLD}, t2c={"内存条": YELLOW_A}
        ).scale(1.2)
        real_mem_text.move_to(ORIGIN).shift(UP * 2)
        real_mem_image = ImageMobject("real-mem.png")
        real_mem_image.next_to(real_mem_text, DOWN, buff=0.4)

        vir_mem_text = Text(
            "操作系统视角: 虚拟内存", color=BLUE, t2w={"虚拟内存": BOLD}, t2c={"虚拟内存": YELLOW_A}
        ).scale(1.2)
        vir_mem_text.move_to(ORIGIN).shift(UP * 2)
        vir_mem_image = ImageMobject("vir-mem.png").scale(1.2)
        vir_mem_image.next_to(vir_mem_text, DOWN, buff=0.4)

        mem_text = Text(
            "硬件视角: 物理内存", color=BLUE, t2w={"物理内存": BOLD}, t2c={"物理内存": YELLOW_A}
        ).scale(1.2)
        mem_text.move_to(ORIGIN).shift(UP * 2)
        mem_image = ImageMobject("mem.png")
        mem_image.next_to(mem_text, DOWN, buff=0.4)

        circut_mem_text = Text(
            "电路视角: 内存电路", color=BLUE, t2w={"内存电路": BOLD}, t2c={"内存电路": YELLOW_A}
        ).scale(1.2)
        circut_mem_text.move_to(ORIGIN).shift(UP * 2)
        circut_mem_image = ImageMobject("circut-mem.png").scale(1.2)
        circut_mem_image.next_to(circut_mem_text, DOWN, buff=0.4)

        self.play(Write(real_mem_text), run_time=1.5)
        self.play(FadeIn(real_mem_image))
        self.wait(2)
        self.play(FadeOut(real_mem_image), FadeOut(real_mem_text))
        self.wait()
        self.play(Write(vir_mem_text), run_time=1.5)
        self.play(FadeIn(vir_mem_image))
        self.wait(2)
        self.play(FadeOut(vir_mem_image), FadeOut(vir_mem_text))
        self.wait()
        self.play(Write(mem_text), run_time=1.5)
        self.play(FadeIn(mem_image))
        self.wait(2)
        self.play(FadeOut(mem_image), FadeOut(mem_text))
        self.wait()
        self.play(Write(circut_mem_text), run_time=1.5)
        self.play(FadeIn(circut_mem_image))
        self.wait(2)
        self.play(FadeOut(circut_mem_image), FadeOut(circut_mem_text))

        new_title = Text("物理内存", color=MAROON_B).scale(1.5)
        new_title.to_edge(UP + LEFT)
        self.play(TransformMatchingStrings(title, new_title))

        # 创建四个矩形，标题分别是物理内存模型、字节与地址空间、地址计算与内存单位、寻址的双重视角
        rect_height = 9 / 4
        rect_width = 16 / 4

        model_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        model_rect.move_to(ORIGIN)
        model_text = Text("物理内存模型", color=BLUE).scale(0.8)
        model_text.next_to(model_rect.get_top(), UP, buff=0.2)
        model_group = VGroup(model_rect, model_text)

        byte_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        byte_rect.move_to(ORIGIN)
        byte_text = Text("字节与地址空间", color=BLUE).scale(0.8)
        byte_text.next_to(byte_rect.get_top(), UP, buff=0.2)
        byte_group = VGroup(byte_rect, byte_text)

        address_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        address_rect.move_to(ORIGIN)
        address_text = Text("字与地址计算", color=BLUE).scale(0.8)
        address_text.next_to(address_rect.get_top(), UP, buff=0.2)
        address_group = VGroup(address_rect, address_text)

        double_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        double_rect.move_to(ORIGIN)
        double_text = Text("寻址的双重视角", color=BLUE).scale(0.8)
        double_text.next_to(double_rect.get_top(), UP, buff=0.2)
        double_group = VGroup(double_rect, double_text)

        # 将四个矩形放置到合适的位置
        model_group.next_to(new_title, DOWN, buff=0.5).align_to(new_title, LEFT).shift(
            RIGHT * 1.8
        )
        byte_group.next_to(model_group, RIGHT, buff=2)
        address_group.next_to(model_group, DOWN, buff=0.5)
        double_group.next_to(address_group, RIGHT, buff=2)

        # 添加所有元素到场景
        self.play(
            ShowCreation(model_rect),
            ShowCreation(byte_rect),
            ShowCreation(address_rect),
            ShowCreation(double_rect),
        )
        self.play(
            Write(model_text), Write(byte_text), Write(address_text), Write(double_text)
        )
        self.wait()
        self.play(Indicate(model_text))
        self.wait()
        self.play(Indicate(byte_text))
        self.wait()
        self.play(Indicate(address_text))
        self.wait()
        self.play(Indicate(double_text))
        self.wait()

        self.play(
            FadeOut(model_group),
            FadeOut(byte_group),
            FadeOut(address_group),
            FadeOut(double_group),
            FadeOut(new_title),
        )


class TotalModel(Scene):
    def construct(self):
        # 创建CPU矩形
        cpu_rect = Rectangle(height=2, width=2)
        cpu_text = Text("CPU")
        cpu_text.move_to(cpu_rect.get_center())
        cpu_group = VGroup(cpu_rect, cpu_text)

        # Create SSD Rectangle
        ssd_rect = Rectangle(height=3.6, width=3.6)
        ssd_text = Text("SSD")
        ssd_text.move_to(ssd_rect.get_center())
        ssd_group = VGroup(ssd_rect, ssd_text)

        # 将CPU和SSD放置到合适的位置
        cpu_group.to_edge(LEFT, buff=3)
        ssd_group.to_edge(RIGHT, buff=3)

        # 添加所有元素到场景
        self.play(ShowCreation(cpu_rect))
        self.play(Write(cpu_text))
        self.play(ShowCreation(ssd_rect))
        self.play(Write(ssd_text))
        self.wait(0.5)

        # 多个箭头从ssd指向cpu
        num_arrows = 5
        data_arrows = []
        for i in range(num_arrows):
            data_arrow = Arrow(
                ssd_rect.get_left() - DOWN * i * 0.5,
                cpu_rect.get_right() - DOWN * i * 0.5,
                buff=0.2,
                stroke_color=BLUE,
            ).shift(DOWN)
            data_arrows.append(data_arrow)
        self.play(*[ShowCreation(data_arrow) for data_arrow in data_arrows])
        self.wait(0.5)
        self.play(*[FadeOut(data_arrow) for data_arrow in data_arrows])

        # CPU矩形和Memory矩形分别往旁边缓慢移动
        self.play(
            cpu_group.animate.shift(LEFT * 1.8), ssd_group.animate.shift(RIGHT * 1.8)
        )

        # 创建Mem矩形
        mem_rect = Rectangle(height=3, width=2.5)
        mem_text = Text("Memory")
        mem_text.move_to(mem_rect.get_center())
        mem_group = VGroup(mem_rect, mem_text)

        mem_group.move_to((cpu_group.get_right() + ssd_group.get_left()) / 2)

        self.play(ShowCreation(mem_rect))
        self.play(Write(mem_text))

        # 多个箭头从ssd指向mem
        num_arrows = 5
        data_arrows = []
        for i in range(num_arrows):
            data_arrow = Arrow(
                ssd_rect.get_left() - DOWN * i * 0.5,
                mem_rect.get_right() - DOWN * i * 0.5,
                buff=0.2,
                stroke_color=BLUE,
            ).shift(DOWN)
            data_arrows.append(data_arrow)
        self.play(*[ShowCreation(data_arrow) for data_arrow in data_arrows])
        self.wait()

        # 在最上面的箭头上添加图片
        image = ImageMobject("bioshock.jpeg")
        image.scale(0.4)
        image.next_to(data_arrows[0].get_top(), UP).shift(RIGHT * 0.12)
        self.play(FadeIn(image))
        self.wait()
        self.play(Indicate(mem_group))
        self.wait()

        mem_text = Text("物理内存(读取数据)", color=MAROON_B).scale(1.5)
        mem_text.to_edge(UP + LEFT)
        self.play(Write(mem_text))
        self.wait()

        # 创建从CPU到Memory的箭头并添加"Address"标签
        cpu2mem_address_arrow = Arrow(
            cpu_rect.get_right() + UP * 0.3,
            mem_rect.get_left() + UP * 0.3,
            buff=0.2,
            stroke_color=ORANGE,
        )
        cpu2mem_address_label = (
            Text("Address")
            .scale(0.8)
            .set_color(ORANGE)
            .next_to(cpu2mem_address_arrow, UP)
        )
        self.play(ShowCreation(cpu2mem_address_arrow))
        self.play(Write(cpu2mem_address_label))
        self.wait()

        # 创建从mem到CPU的箭头并添加"Data"标签
        mem2cpu_data_arrow = Arrow(
            mem_rect.get_left() + DOWN * 0.3,
            cpu_rect.get_right() + DOWN * 0.3,
            buff=0.2,
            stroke_color=BLUE,
        )
        mem2cpu_data_label = (
            Text("Data").scale(0.8).set_color(BLUE).next_to(mem2cpu_data_arrow, DOWN)
        )
        self.play(ShowCreation(mem2cpu_data_arrow))
        self.play(Write(mem2cpu_data_label))
        self.wait()

        mem_text_1 = Text("物理内存(写入数据)", color=MAROON_B).scale(1.5)
        mem_text_1.to_edge(UP + LEFT)
        self.play(TransformMatchingStrings(mem_text, mem_text_1))
        self.play(
            FadeOut(cpu2mem_address_arrow),
            FadeOut(cpu2mem_address_label),
            FadeOut(mem2cpu_data_arrow),
            FadeOut(mem2cpu_data_label),
        )

        cpu2mem_data_arrow = Arrow(
            cpu_rect.get_right() + DOWN * 0.3,
            mem_rect.get_left() + DOWN * 0.3,
            buff=0.2,
            stroke_color=BLUE,
        )
        cpu2mem_data_label = (
            Text("Data").scale(0.8).set_color(BLUE).next_to(cpu2mem_data_arrow, DOWN)
        )

        self.play(ShowCreation(cpu2mem_address_arrow))
        self.play(Write(cpu2mem_address_label))
        self.wait()
        self.play(ShowCreation(cpu2mem_data_arrow))
        self.play(Write(cpu2mem_data_label))
        self.wait()

        # 全部淡出
        self.play(
            FadeOut(cpu_group),
            FadeOut(ssd_group),
            FadeOut(mem_group),
            FadeOut(cpu2mem_address_arrow),
            FadeOut(cpu2mem_address_label),
            FadeOut(cpu2mem_data_arrow),
            FadeOut(cpu2mem_data_label),
            FadeOut(image),
            FadeOut(mem_text_1),
            *[FadeOut(data_arrow) for data_arrow in data_arrows],
        )


class Model1(Scene):
    def construct(self):
        # 创建最简单的内存模型
        simple_table = VGroup()
        simple_table_rect = VGroup()
        simple_table_label = VGroup()
        simple_table.add(simple_table_rect)
        simple_table.add(simple_table_label)
        for i in range(8):
            rect = Rectangle(height=0.8, width=2)
            rect.shift(UP * i * 0.8)
            # 然后，定义标签的最终位置（矩形内部的右下角）
            label = Text(str(i), font_size=15, color=BLUE).scale(2)
            simple_table_rect.add(rect)
            simple_table_label.add(label)

        simple_table_rect.arrange(DOWN, aligned_edge=LEFT, buff=0)
        simple_table_rect.move_to(ORIGIN)

        # 在排列完矩形后，更新标签的位置
        for i, label in enumerate(simple_table_label):
            label.next_to(simple_table_rect[i], LEFT)

        self.play(FadeIn(simple_table_rect))
        self.wait(1)

        for label in simple_table_label:
            self.play(Write(label, run_time=0.3))

        self.wait(1)

        # 更新标签的位置
        for i, label in enumerate(simple_table_label):
            target_position = (
                simple_table_rect[i].get_corner(DOWN + RIGHT) + UP * 0.2 + LEFT * 0.2
            )
            self.play(label.animate.move_to(target_position), run_time=0.3)

        # 左上角添加内存大小信息
        byte_arr_text = Text("字节数组").to_edge(UP + LEFT).scale(1.2)
        byte_addressed_text = Text("按字节编址").to_edge(UP + LEFT).scale(1.2)
        self.play(Write(byte_arr_text))
        self.wait(1)
        self.play(
            TransformMatchingStrings(byte_arr_text, byte_addressed_text, run_time=1)
        )
        self.wait(1)
        byte_line_text = (
            Text("""1"行"(Line) 为 1字节(Byte)""", color=YELLOW)
            .scale(0.8)
            .next_to(byte_arr_text, DOWN, buff=0.2)
            .align_to(byte_arr_text, LEFT)
        )
        self.play(Write(byte_line_text))
        self.wait(2)

        # 创建箭头
        arrow = Arrow(
            simple_table_rect[3].get_right(),
            simple_table_rect[3].get_right() + RIGHT * 1.6,
            buff=0.2,
            stroke_color=ORANGE,
        )
        self.play(FlashAround(simple_table_rect[3]), run_time=2)
        self.play(ShowCreation(arrow))

        # simple_table中的其中一个矩形指向一个单行八列的表格
        bit_table = VGroup()
        for i in range(8):
            bit_rect = Rectangle(height=0.5, width=0.5)
            if i == 0 or i == 1 or i == 3 or i == 7:
                bit_label = (
                    Text("0", color=YELLOW).scale(0.4).move_to(bit_rect.get_center())
                )
            else:
                bit_label = (
                    Text("1", color=YELLOW).scale(0.4).move_to(bit_rect.get_center())
                )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(arrow, RIGHT)
            else:
                bit.next_to(bit_table[-1], RIGHT, buff=0)
            bit_table.add(bit)

        self.play(FadeIn(bit_table))
        self.wait(2)

        # 大括号
        brace = Brace(bit_table, DOWN, buff=0.1)
        brace_text = (
            Text("8个位(bit)", color=YELLOW_C)
            .scale(0.8)
            .next_to(brace, DOWN, buff=0.2)
            .align_to(brace, ORIGIN)
        )
        self.play(ShowCreation(brace), Write(brace_text))
        self.wait(2)

        # 箭头指向解释位的概念
        bit_arrow = Arrow(
            brace_text.get_bottom(),
            brace_text.get_bottom() + DOWN * 1.6,
            buff=0.2,
            stroke_color=ORANGE,
        )
        bit_text = (
            Text("计算机中最小的存储单位", color=BLUE)
            .scale(0.8)
            .next_to(bit_arrow, DOWN, buff=0.2)
            .align_to(bit_arrow, LEFT)
            .shift(LEFT * 2)
        )
        self.play(ShowCreation(bit_arrow), Write(bit_text))
        self.wait(2)
        for i in range(8):
            self.play(Indicate(bit_table[i]), run_time=0.2)
        self.wait(2)

        byte_bit_text = (
            Text("1字节(Byte) = 8位(bit)", color=BLUE)
            .scale(0.8)
            .next_to(bit_table, UP, buff=0.2)
            .align_to(bit_table, ORIGIN)
        )

        self.play(Write(byte_bit_text))
        self.wait(2)

        # 淡出操作
        byte_bit_text.generate_target()
        byte_bit_text.target.next_to(byte_line_text, DOWN, buff=0.2).align_to(
            byte_line_text, LEFT
        )
        self.play(MoveToTarget(byte_bit_text))
        self.play(
            FadeOut(arrow),
            FadeOut(bit_table),
            FadeOut(simple_table),
            FadeOut(brace),
            FadeOut(brace_text),
            FadeOut(bit_arrow),
            FadeOut(bit_text),
        )

        # 讲解位数访问地址数量的关系，从一位开始，接着是两位和三位
        bit_labels_1 = self.create_bit_labels(1)
        bit_labels_1_back = self.create_bit_labels(1)
        memory_addresses_1 = self.create_memory_addresses(1)
        arrows_1 = self.create_arrows(bit_labels_1, memory_addresses_1)
        bit_labels_2 = self.create_bit_labels(2)
        bit_labels_2_back = self.create_bit_labels(2)
        memory_addresses_2 = self.create_memory_addresses(2)
        arrows_2 = self.create_arrows(bit_labels_2, memory_addresses_2)
        bit_labels_3 = self.create_bit_labels(3)
        memory_addresses_3 = self.create_memory_addresses(3)
        arrows_3 = self.create_arrows(bit_labels_3, memory_addresses_3)

        bit_area_1 = VGroup(
            *bit_labels_1,
            *arrows_1,
            *memory_addresses_1,
        )
        bit_area_2 = VGroup(
            *bit_labels_2,
            *arrows_2,
            *memory_addresses_2,
        )
        bit_area_3 = VGroup(
            *bit_labels_3,
            *arrows_3,
            *memory_addresses_3,
        )
        bit_area_1.to_edge(UP, buff=2.5)
        bit_area_2.to_edge(UP, buff=2.5)
        bit_area_3.to_edge(UP, buff=2.5)

        # 创建情况
        bit_1 = Text("1位", t2c={"1": BLUE_A})
        bit_2 = Text("2位", t2c={"2": BLUE_A})
        bit_3 = Text("3位", t2c={"3": BLUE_A})
        bit_k = Text("y位", t2c={"y": BLUE_A})

        arrow_1 = Text("<=>")
        arrow_2 = Text("<=>")
        arrow_3 = Text("<=>")
        arrow_k = Text("<=>")

        address_1 = Text("2个地址", t2c={"2": RED_A})
        address_2 = Text("4个地址", t2c={"4": RED_A})
        address_3 = Text("8个地址", t2c={"8": RED_A})
        address_k = Text("x个地址", t2c={"x": RED_A})

        # 排列情况
        situation_1 = (
            VGroup(bit_1, arrow_1, address_1).arrange(RIGHT, buff=0.2).scale(0.8)
        )
        situation_2 = (
            VGroup(bit_2, arrow_2, address_2).arrange(RIGHT, buff=0.2).scale(0.8)
        )
        situation_3 = (
            VGroup(bit_3, arrow_3, address_3).arrange(RIGHT, buff=0.2).scale(0.8)
        )

        # 1位
        for bit_label, arrow, memory_address in zip(
            bit_labels_1, arrows_1, memory_addresses_1
        ):
            self.play(Write(bit_label))
            self.play(Write(arrow))
            self.play(Write(memory_address))
        self.wait()
        situation_1.next_to(bit_area_1, RIGHT, buff=0.5)
        self.play(Write(situation_1))
        self.wait()

        # 2位
        bit_labels_1[0].save_state()
        bit_labels_1[1].save_state()
        self.play(
            Transform(bit_labels_1[0], bit_labels_2[0]),
            Transform(bit_labels_1[1], bit_labels_2[1]),
            Transform(arrows_1[0], arrows_2[0]),
            Transform(arrows_1[1], arrows_2[1]),
        )
        for bit_label, arrow, memory_address in zip(
            bit_labels_2[2:], arrows_2[2:], memory_addresses_2[2:]
        ):
            self.play(Write(bit_label))
            self.play(Write(arrow))
            self.play(Write(memory_address))
        self.wait()
        situation_2.next_to(situation_1, DOWN, buff=0.4)
        self.play(Write(situation_2))
        self.wait()

        # 3位
        bit_labels_2[2].save_state()
        bit_labels_2[3].save_state()
        self.play(
            Transform(bit_labels_1[0], bit_labels_3[0]),
            Transform(bit_labels_1[1], bit_labels_3[1]),
            Transform(bit_labels_2[2], bit_labels_3[2]),
            Transform(bit_labels_2[3], bit_labels_3[3]),
            Transform(arrows_1[0], arrows_3[0]),
            Transform(arrows_1[1], arrows_3[1]),
            Transform(arrows_2[2], arrows_3[2]),
            Transform(arrows_2[3], arrows_3[3]),
        )
        for bit_label, arrow, memory_address in zip(
            bit_labels_3[4:], arrows_3[4:], memory_addresses_3[4:]
        ):
            self.play(Write(bit_label))
            self.play(Write(arrow))
            self.play(Write(memory_address))
        self.wait()
        situation_3.next_to(situation_2, DOWN, buff=0.4)
        self.play(Write(situation_3))
        self.wait()

        # 三个区域分别进行移动
        self.play(
            Restore(bit_labels_1[0]),
            Restore(bit_labels_1[1]),
            Restore(bit_labels_2[2]),
            Restore(bit_labels_2[3]),
        )
        bit_area_1_rect = SurroundingRectangle(
            bit_area_1, color=WHITE, buff=0.3, stroke_width=1
        )
        bit_area_2_rect = SurroundingRectangle(
            bit_area_2, color=WHITE, buff=0.3, stroke_width=1
        )
        bit_area_3_rect = SurroundingRectangle(
            bit_area_3, color=WHITE, buff=0.3, stroke_width=1
        )
        bit_area_1_all = VGroup(bit_area_1, bit_area_1_rect)
        bit_area_2_all = VGroup(bit_area_2, bit_area_2_rect)
        bit_area_3_all = VGroup(bit_area_3, bit_area_3_rect)
        bit_area_1_all.generate_target()
        bit_area_2_all.generate_target()
        bit_area_3_all.generate_target()
        bit_area_1_all.target.to_edge(LEFT, buff=0.1).shift(DOWN * 0.1)
        bit_area_2_all.target.next_to(bit_area_1_all.target, DOWN, buff=0.78)
        bit_area_3_all.target.next_to(bit_area_1_all.target, RIGHT, buff=0.2).align_to(
            bit_area_1_all.target, UP
        )
        self.play(
            MoveToTarget(bit_area_1_all),
            MoveToTarget(bit_area_2_all),
            MoveToTarget(bit_area_3_all),
        )
        self.play(
            ShowCreation(bit_area_1_rect),
            ShowCreation(bit_area_2_rect),
            ShowCreation(bit_area_3_rect),
        )

        # 创建点状列表
        ellipsis = (
            Text("...").next_to(situation_3, DOWN, buff=0.4).rotate(PI / 2).scale(0.8)
        )
        situation_k = (
            VGroup(bit_k, arrow_k, address_k)
            .arrange(RIGHT, buff=0.2)
            .scale(0.8)
            .next_to(ellipsis, DOWN, buff=0.4)
        )
        self.play(Write(ellipsis))
        self.wait()
        self.play(Write(situation_k))
        self.wait()

        situations = VGroup(
            situation_1,
            situation_2,
            situation_3,
            ellipsis,
            situation_k,
        )
        situations_rect = SurroundingRectangle(situations, buff=0.2)
        situations_with_rect = VGroup(situations, situations_rect)
        situations_with_rect.generate_target()
        situations_with_rect.target.shift(LEFT * 1.5)

        self.play(ShowCreation(situations_rect))
        self.wait()
        self.play(MoveToTarget(situations_with_rect))
        self.wait()

        # 创建公式
        tex_arrow_1 = Tex("\\Rightarrow").next_to(situation_1, RIGHT, buff=0.6)
        tex_arrow_2 = Tex("\\Rightarrow").next_to(situation_2, RIGHT, buff=0.6)
        tex_arrow_3 = Tex("\\Rightarrow").next_to(situation_3, RIGHT, buff=0.6)
        tex_arrow_k = Tex("\\Rightarrow").next_to(situation_k, RIGHT, buff=0.6)
        formula_1 = (
            Tex("2^{{1}} = {{2}}").scale(0.8).next_to(tex_arrow_1, RIGHT, buff=0.6)
        )
        formula_2 = (
            Tex("2^{{2}} = {{4}}").scale(0.8).next_to(tex_arrow_2, RIGHT, buff=0.6)
        )
        formula_3 = (
            Tex("2^{{3}} = {{8}}").scale(0.8).next_to(tex_arrow_3, RIGHT, buff=0.6)
        )
        formula_k = (
            Tex("2^{{y}} = {{x}}").scale(0.8).next_to(tex_arrow_k, RIGHT, buff=0.6)
        )
        formula_1.set_color_by_tex("1", BLUE_A)
        formula_1.set_color_by_tex("2", RED_A)
        formula_2.set_color_by_tex("2", BLUE_A)
        formula_2.set_color_by_tex("4", RED_A)
        formula_3.set_color_by_tex("3", BLUE_A)
        formula_3.set_color_by_tex("8", RED_A)
        formula_k.set_color_by_tex("y", BLUE_A)
        formula_k.set_color_by_tex("x", RED_A)
        formula_ellipsis = (
            Text("...").scale(0.8).next_to(formula_3, DOWN, buff=0.4).rotate(PI / 2)
        )
        self.play(Write(tex_arrow_1))
        self.play(Write(formula_1))
        self.wait()
        self.play(Write(tex_arrow_2))
        self.play(Write(formula_2))
        self.wait()
        self.play(Write(tex_arrow_3))
        self.play(Write(formula_3))
        self.wait()
        self.play(Write(formula_ellipsis))
        self.wait()
        self.play(Write(tex_arrow_k))
        self.play(Write(formula_k))
        self.wait()

        # Log公式
        log_formula_1 = (
            Tex("{{1}} = \\log_2{{2}}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"1": BLUE_A, "2": RED_A})
            .next_to(tex_arrow_1, RIGHT, buff=0.6)
        )
        log_formula_2 = (
            Tex("{{2}} = \\log_2{{4}}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"2": BLUE_A, "4": RED_A})
            .next_to(tex_arrow_2, RIGHT, buff=0.6)
        )
        log_formula_3 = (
            Tex("3 = \\log_2{8}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"3": BLUE_A, "8": RED_A})
            .next_to(tex_arrow_3, RIGHT, buff=0.6)
        )
        log_formula_k = (
            Tex("y = \\log_2{x}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"y": BLUE_A, "x": RED_A})
            .next_to(tex_arrow_k, RIGHT, buff=0.6)
        )

        self.play(TransformMatchingTex(formula_1, log_formula_1))
        self.wait()
        self.play(TransformMatchingTex(formula_2, log_formula_2))
        self.wait()
        self.play(TransformMatchingTex(formula_3, log_formula_3))
        self.wait()
        self.play(TransformMatchingTex(formula_k, log_formula_k))
        self.wait()
        self.play(
            FadeOut(situations_rect),
            FadeOut(situations),
            FadeOut(tex_arrow_1),
            FadeOut(tex_arrow_2),
            FadeOut(tex_arrow_3),
            FadeOut(tex_arrow_k),
            FadeOut(log_formula_1),
            FadeOut(log_formula_2),
            FadeOut(log_formula_3),
            FadeOut(formula_ellipsis),
        )
        log_formula_k.generate_target()
        log_formula_k.target.scale(1.2).shift(DOWN * 1.6 + LEFT * 2.2)
        self.play(MoveToTarget(log_formula_k))

        # 坐标上函数演示
        axe_config = {
            "x_range": (0, 10),
            "y_range": (-1, 4),
            "axis_config": {"include_tip": True},
        }
        axes = Axes(**axe_config).scale(0.68)
        axes.get_x_axis().set_color(RED_A)
        axes.get_y_axis().set_color(BLUE_A)
        axes.add_coordinate_labels()
        axes.next_to(log_formula_k, UP, buff=0.5)

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph会返回传入方程的图像
        log_graph = axes.get_graph(
            lambda x: np.log2(x), color=YELLOW_A, x_range=[1, 10]
        )
        self.play(ShowCreation(log_graph))
        self.wait()

        # 创造一个点，从(1,0)开始s
        dot = Dot(fill_color=GREEN_A).move_to(axes.c2p(1, 0))
        self.play(FadeIn(dot))
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )

        # For (2, 1)
        self.play(
            MoveAlongPath(
                dot,
                axes.get_graph(lambda t: np.log2(t) if t > 0 else 0, x_range=[1, 2]),
                rate_func=linear,
            ),
        )
        self.wait()
        coord_label = (
            Tex("(2, 1)")
            .set_color_by_tex_to_color_map({"1": BLUE_A, "2": RED_A})
            .next_to(dot, UP)
        )
        self.play(Write(coord_label))
        self.wait()
        self.play(Indicate(coord_label[3]), Indicate(log_formula_k[0]))
        self.wait()
        self.play(*[Indicate(txt) for txt in bit_labels_1])
        self.wait()
        self.play(Indicate(coord_label[1]), Indicate(log_formula_k[6]))
        self.wait()
        self.play(*[Indicate(txt) for txt in memory_addresses_1])
        self.wait()
        self.play(FadeOut(coord_label))

        # For (4, 2)
        self.play(
            MoveAlongPath(
                dot,
                axes.get_graph(lambda t: np.log2(t) if t > 0 else 0, x_range=[2, 4]),
                rate_func=linear,
            ),
        )
        self.wait()
        coord_label = (
            Tex("(4, 2)")
            .set_color_by_tex_to_color_map({"2": BLUE_A, "4": RED_A})
            .next_to(dot, UP)
        )
        self.play(Write(coord_label))
        self.wait()
        self.play(Indicate(coord_label[3]), Indicate(log_formula_k[0]))
        self.wait()
        self.play(*[Indicate(txt) for txt in bit_labels_2])
        self.wait()
        self.play(Indicate(coord_label[1]), Indicate(log_formula_k[6]))
        self.wait()
        self.play(*[Indicate(txt) for txt in memory_addresses_2])
        self.wait()
        self.play(FadeOut(coord_label))

        # For (8, 3)
        self.play(
            MoveAlongPath(
                dot,
                axes.get_graph(lambda t: np.log2(t) if t > 0 else 0, x_range=[4, 8]),
                rate_func=linear,
            ),
        )
        self.wait()
        coord_label = (
            Tex("(8, 3)")
            .set_color_by_tex_to_color_map({"3": BLUE_A, "8": RED_A})
            .next_to(dot, UP)
        )
        self.play(Write(coord_label))
        self.wait()
        self.play(Indicate(coord_label[3]), Indicate(log_formula_k[0]))
        self.wait()
        self.play(*[Indicate(txt) for txt in bit_labels_3])
        self.wait()
        self.play(Indicate(coord_label[1]), Indicate(log_formula_k[6]))
        self.wait()
        self.play(*[Indicate(txt) for txt in memory_addresses_3])
        self.wait()
        # 淡出
        self.play(
            FadeOut(axes),
            FadeOut(log_graph),
            FadeOut(dot),
            FadeOut(h_line),
            FadeOut(v_line),
            FadeOut(coord_label),
            FadeOut(log_formula_k),
        )
        self.play(
            FadeOut(bit_area_1_all),
            FadeOut(bit_area_2_all),
            FadeOut(bit_area_3_all),
            FadeOut(byte_addressed_text),
            FadeOut(byte_line_text),
            FadeOut(byte_bit_text),
        )

    def create_bit_labels(self, num_bits):
        labels = []
        for i in range(2**num_bits):
            bit_string = format(i, f"0{num_bits}b")
            label = (
                Text(bit_string, color=BLUE_A)
                .scale(1)
                .move_to(LEFT * 1 + DOWN * i * 0.6)
            )
            labels.append(label)
        return labels

    def create_memory_addresses(self, num_bits):
        addresses = []
        for i in range(2**num_bits):
            address_label = (
                Tex(f"m_{i}", color=RED_A)
                .scale(0.8)
                .move_to(RIGHT * 1 + DOWN * i * 0.6)
            )
            rect = SurroundingRectangle(
                address_label, color=WHITE, buff=0.1, stroke_width=1.5
            )
            grouped_address = VGroup(address_label, rect)
            addresses.append(grouped_address)
        return addresses

    def create_arrows(self, bit_labels, memory_addresses):
        arrows = []
        for lbl, addr in zip(bit_labels, memory_addresses):
            arrow = Arrow(
                lbl.get_right(),
                addr.get_left(),
                buff=0.2,
                stroke_color=ORANGE,
                stroke_width=4,
            ).scale(0.8)
            arrows.append(arrow)
        return arrows


class Model2(Scene):
    def construct(self):
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
        byte_bit_text = (
            Text("1字节(Byte) = 8位(bit)", color=BLUE)
            .scale(0.7)
            .next_to(byte_addressed_text, DOWN, buff=0.15)
            .align_to(byte_addressed_text, LEFT)
        )
        self.play(Write(byte_bit_text))
        self.wait()
        byte_line_text = (
            Text("""1"行"(Line) 为 1字节(Byte)""", color=YELLOW)
            .scale(0.7)
            .next_to(byte_bit_text, DOWN, buff=0.15)
            .align_to(byte_bit_text, LEFT)
        )
        self.play(Write(byte_line_text))
        self.wait()

        # 定义参数
        visible_rows_top = 8
        visible_rows_bottom = 4
        total_rows = 64
        cell_height = 0.5
        cell_width = 2
        omit_height = 1

        # 创建表格
        table = VGroup()  # 用于存储所有的矩形（单元格）

        # 建立顶部的单元格
        for i in range(visible_rows_top):
            rect = Rectangle(height=cell_height, width=cell_width)
            rect.shift(UP * i * cell_height)
            label = Text(str(i), font_size=25, color=BLUE).move_to(
                rect.get_corner(DOWN + RIGHT) + UP * 0.15 + LEFT * 0.15
            )
            cell_group = VGroup(rect, label)
            table.add(cell_group)

        # 建立中间的单元格，代表省略的部分
        omit_rect = Rectangle(height=omit_height, width=cell_width)
        omit_rect.shift(UP * visible_rows_top * cell_height)
        omit_label = (
            Text("...", font_size=25).rotate(PI / 2).move_to(omit_rect.get_center())
        )
        omit_cell_group = VGroup(omit_rect, omit_label)
        table.add(omit_cell_group)

        # 建立底部的单元格
        for i in range(visible_rows_bottom):
            rect = Rectangle(height=cell_height, width=cell_width)
            rect.shift(DOWN * i * cell_height + DOWN * omit_height)
            label = Text(
                str(total_rows - visible_rows_bottom + i), font_size=25, color=BLUE
            ).move_to(rect.get_corner(DOWN + RIGHT) + UP * 0.15 + LEFT * 0.15)
            cell_group = VGroup(rect, label)
            table.add(cell_group)

        # 将表格移到中心
        table.arrange(DOWN, aligned_edge=LEFT, buff=0)
        table.move_to(ORIGIN + RIGHT * 2.5)

        # 显示所有元素
        self.play(FadeIn(table))
        self.wait()
        # 创建一个大括号，放在table的右侧
        brace = Brace(table, RIGHT)
        # 如果你还想添加一个标签或文字在大括号旁边
        brace_label = brace.get_text("64行").shift(RIGHT * 0.1)
        # 显示在场景中
        self.play(FadeIn(brace))
        self.wait()
        self.play(Write(brace_label))
        self.wait()
        self.play(FadeOut(brace), FadeOut(brace_label))
        self.wait()

        # 定义公式的各部分
        formula = (
            Tex("\\log_2{{64}}=\\log_2{2^{{6}}}={{6}}")
            .scale(0.7)
            .set_color_by_tex_to_color_map({"64": RED_A, "6": BLUE_A})
            .next_to(byte_line_text, DOWN, buff=0.2)
            .align_to(byte_line_text, LEFT)
        )
        explanation = (
            Text("6位<=>64个地址", t2c={"6": BLUE_A, "64": RED_A})
            .next_to(byte_line_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(byte_line_text, LEFT)
        )

        # 按顺序播放公式的动画
        self.play(Write(formula, run_time=3))
        self.wait()
        self.play(ReplacementTransform(formula, explanation))
        self.wait()

        # 单行六列的表格
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
        self.wait(2)

        table_content = r"""
        \begin{tabular}{|c|c|c|c|c|c|c|c|}
        \hline
        32 & 16 & 8 & 4 & 2 & 1 \\
        \hline
        $2^5$ & $2^4$ & $2^3$ & $2^2$ & $2^1$ & $2^0$ \\
        \hline
        \end{tabular}
        """

        bin_dec_table = (
            Tex(table_content)
            .scale(0.5)
            .to_edge(UP)
            .shift(LEFT * 1 + DOWN * 0.5)
            .set_color(GREEN_B)
        )

        self.play(Write(bin_dec_table))
        self.wait(2)

        # 访存计算演示
        bin_expansion = VGroup()
        for i in range(6):
            power_of_two = Tex(f"2^{{ {5-i} }}").scale(0.9)
            times_sign = Tex("\\times")
            bit_val = Text("0").scale(0.9)
            if i != 0:
                plus_sign = Tex("+").next_to(bin_expansion, RIGHT, buff=0.1)
                bin_expansion.add(plus_sign)

            term = VGroup(power_of_two, times_sign, bit_val)
            term.arrange(RIGHT, buff=0.1)
            term.next_to(bin_expansion, RIGHT, buff=0.1)
            bin_expansion.add(term)

        bin_expansion.scale(0.8).next_to(bit_table_6, DOWN, buff=0.25).shift(
            RIGHT * 1.5
        )
        self.play(Write(bin_expansion))
        self.wait()

        for i in range(6):
            # 获取bit_table_6中的位值
            bit_val = bit_table_6[i][1]
            # 动画移动
            self.play(TransformFromCopy(bit_val, bin_expansion[2 * i][2]))
            # 更新二进制展开式中对应的值
            new_text = (
                Text(bit_val.text, color=YELLOW)
                .scale(0.8)
                .move_to(bin_expansion[2 * i][2].get_center())
            )
            self.play(Transform(bin_expansion[2 * i][2], new_text), run_time=0.25)
        self.wait()

        bin_expansion_result = (
            Tex("= 0 + 0 + 0 + 0 + 0 + 0 = 0")
            .scale(0.8)
            .next_to(bin_expansion, DOWN, buff=0.15)
            .align_to(bin_expansion, RIGHT)
            .shift(RIGHT * 0.2)
        )
        self.play(Write(bin_expansion_result))
        self.wait()

        # 箭头指向第一行
        addressing_arrow = Arrow(
            bin_expansion_result.get_right() + RIGHT * 0.1,
            table[0].get_left() + LEFT * 0.1,
            buff=0.1,
            stroke_width=2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(addressing_arrow))
        self.play(Indicate(table[0]))
        self.wait()
        self.play(FadeOut(addressing_arrow))
        self.wait()

        # 创建一个新的Text对象，并设置其位置为原始bit_label的位置
        new_bit_label_5 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_6[5][1].get_center())
        )
        self.play(ReplacementTransform(bit_table_6[5][1], new_bit_label_5))
        self.play(Indicate(bit_table_6[5]))
        self.wait()

        new_text = (
            Text(new_bit_label_5.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion[10][2].get_center())
        )
        self.play(Transform(bin_expansion[10][2], new_text), run_time=0.25)
        self.wait()
        self.play(Indicate(bin_expansion[10][2]))
        self.wait()

        bin_expansion_result_1 = (
            Tex("= 0 + 0 + 0 + 0 + 0 + 1 = 1")
            .scale(0.8)
            .next_to(bin_expansion, DOWN, buff=0.15)
            .align_to(bin_expansion, RIGHT)
            .shift(RIGHT * 0.2)
        )
        self.play(ReplacementTransform(bin_expansion_result, bin_expansion_result_1))
        self.wait()

        addressing_arrow = Arrow(
            bin_expansion_result_1.get_right() + RIGHT * 0.1,
            table[1].get_left() + LEFT * 0.1,
            buff=0.1,
            stroke_width=2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(addressing_arrow))
        self.play(Indicate(table[1]))
        self.wait()
        self.play(FadeOut(addressing_arrow))

        # 创建一个新的Text对象，并设置其位置为原始bit_label的位置
        new_bit_label_3 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_6[3][1].get_center())
        )
        self.play(ReplacementTransform(bit_table_6[3][1], new_bit_label_3))
        self.play(Indicate(bit_table_6[3]))
        self.wait()

        new_text = (
            Text(new_bit_label_3.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion[6][2].get_center())
        )
        self.play(Transform(bin_expansion[6][2], new_text), run_time=0.25)
        self.wait()
        self.play(Indicate(bin_expansion[6][2]))
        self.wait()

        bin_expansion_result_2 = (
            Tex("= 0 + 0 + 0 + 4 + 0 + 1 = 5")
            .scale(0.8)
            .next_to(bin_expansion, DOWN, buff=0.15)
            .align_to(bin_expansion, RIGHT)
            .shift(RIGHT * 0.2)
        )
        self.play(ReplacementTransform(bin_expansion_result_1, bin_expansion_result_2))
        self.wait()

        addressing_arrow = Arrow(
            bin_expansion_result_2.get_right() + RIGHT * 0.1,
            table[5].get_left() + LEFT * 0.1,
            buff=0.1,
            stroke_width=2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(addressing_arrow))
        self.play(Indicate(table[5]))
        self.wait()
        self.play(FadeOut(addressing_arrow))

        # 创建一个新的Text对象，并设置其位置为原始bit_label的位置
        new_bit_label_0 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_6[0][1].get_center())
        )
        new_bit_label_1 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_6[1][1].get_center())
        )
        new_bit_label_2 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_6[2][1].get_center())
        )

        self.play(
            ReplacementTransform(bit_table_6[0][1], new_bit_label_0),
            ReplacementTransform(bit_table_6[1][1], new_bit_label_1),
            ReplacementTransform(bit_table_6[2][1], new_bit_label_2),
        )

        new_text_0 = (
            Text(new_bit_label_0.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion[0][2].get_center())
        )
        self.play(Transform(bin_expansion[0][2], new_text_0), run_time=0.25)
        self.wait()

        new_text_1 = (
            Text(new_bit_label_1.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion[2][2].get_center())
        )
        self.play(Transform(bin_expansion[2][2], new_text_1), run_time=0.25)
        self.wait()

        new_text_2 = (
            Text(new_bit_label_2.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion[4][2].get_center())
        )
        self.play(Transform(bin_expansion[4][2], new_text_2), run_time=0.25)
        self.wait()
        self.play(
            Indicate(bin_expansion[0][2]),
            Indicate(bin_expansion[4][2]),
            Indicate(bin_expansion[2][2]),
        )
        self.wait()

        bin_expansion_result_3 = (
            Tex("= 32 + 16 + 8 + 4 + 0 + 1 = 61")
            .scale(0.8)
            .next_to(bin_expansion, DOWN, buff=0.15)
            .align_to(bin_expansion, RIGHT)
            .shift(RIGHT * 0.2)
        )
        self.play(ReplacementTransform(bin_expansion_result_2, bin_expansion_result_3))
        self.wait()

        addressing_arrow = Arrow(
            bin_expansion_result_3.get_right() + RIGHT * 0.1,
            table[-3].get_left() + LEFT * 0.1,
            buff=0.1,
            stroke_width=2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(addressing_arrow))
        self.play(Indicate(table[-3]))
        self.wait()
        self.play(FadeOut(addressing_arrow))
        self.play(FadeOut(bin_expansion_result_3), FadeOut(bin_expansion))
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

        # 一字为1字节
        word_byte_text_1 = (
            Text("1字(Word) = 1字节(Byte) = 8位(bit)", color=RED_D)
            .scale(0.7)
            .next_to(word_addressed_text, DOWN, buff=0.15)
            .align_to(word_addressed_text, LEFT)
        )
        self.play(Write(word_byte_text_1))
        self.wait()

        word_line_text = (
            Text("""1"行"(Line) 为 1字(Word)""", color=YELLOW)
            .scale(0.7)
            .next_to(word_byte_text_1, DOWN, buff=0.15)
            .align_to(word_byte_text_1, LEFT)
        )
        self.play(Write(word_line_text))
        self.wait()

        # 分别闪烁前八行和后四行
        for i in range(3):
            self.play(FlashAround(table[i]))
        for i in range(3, 8):
            self.play(FlashAround(table[i]), run_time=0.3)
        for i in reversed(range(4)):
            self.play(FlashAround(table[-1 - i], run_time=0.4))
        self.wait()

        # 复制解释和6位表格
        explanation_copy = explanation.copy()
        bit_table_6_copy = bit_table_6.copy()
        explanation_copy.next_to(word_line_text, DOWN, buff=0.2).align_to(
            word_line_text, LEFT
        )
        bit_table_6_copy.next_to(explanation_copy, DOWN, buff=0.1).align_to(
            explanation_copy, LEFT
        )
        self.play(Write(explanation_copy), FadeIn(bit_table_6_copy))
        self.wait()

        self.play(FadeOut(explanation_copy), FadeOut(bit_table_6_copy))
        self.wait()

        # 一字为4字节
        word_byte_text_4 = (
            Text("1字(Word) = 4字节(Byte) = 32位(bit)", color=RED_D)
            .scale(0.7)
            .next_to(word_addressed_text, DOWN, buff=0.15)
            .align_to(word_addressed_text, LEFT)
        )
        self.play(ReplacementTransform(word_byte_text_1, word_byte_text_4))
        self.wait()

        # 以四行为单位进行闪烁
        for i in range(2):
            self.play(FlashAround(table[i * 4 : (i + 1) * 4]))
        # 最后四行一起闪烁
        self.play(FlashAround(table[-4:]))

        word_line_text_4 = (
            Text("""4"行"(Line) 为 1字(Word)""", color=YELLOW)
            .scale(0.7)
            .next_to(word_byte_text_1, DOWN, buff=0.15)
            .align_to(word_byte_text_1, LEFT)
        )
        self.play(TransformMatchingStrings(word_line_text, word_line_text_4))
        self.wait()

        # 创建矩形覆盖前四行
        one_group_rect = Rectangle(
            height=4 * cell_height,
            width=cell_width,
            fill_opacity=0,
            stroke_color=RED,
            stroke_width=4,
        )
        # 设置矩形的位置
        one_group_rect.next_to(table[4], UP, buff=0, aligned_edge=LEFT).shift(UP * 0.01)
        one_group_rect_label = (
            Text("0", color=RED)
            .scale(0.7)
            .next_to(one_group_rect, LEFT, buff=0.2)
            .align_to(one_group_rect, ORIGIN)
        )

        # 创建矩形覆盖中间四行
        two_group_rect = Rectangle(
            height=4 * cell_height,
            width=cell_width,
            fill_opacity=0,
            stroke_color=GREEN,
            stroke_width=4,
        )
        # 设置矩形的位置
        two_group_rect.next_to(table[8], UP, buff=0, aligned_edge=LEFT).shift(
            DOWN * 0.01
        )
        two_group_rect_label = (
            Text("1", color=GREEN)
            .scale(0.7)
            .next_to(two_group_rect, LEFT, buff=0.2)
            .align_to(two_group_rect, ORIGIN)
        )

        # 创建矩形覆盖后四行
        three_group_rect = Rectangle(
            height=4 * cell_height,
            width=cell_width,
            fill_opacity=0,
            stroke_color=BLUE,
            stroke_width=4,
        )
        # 设置矩形的位置
        three_group_rect.next_to(table[-1], UP, buff=0, aligned_edge=LEFT).shift(
            DOWN * cell_height
        )
        three_group_rect_label = (
            Text("15", color=BLUE)
            .scale(0.7)
            .next_to(three_group_rect, LEFT, buff=0.2)
            .align_to(three_group_rect, ORIGIN)
        )

        self.play(
            ShowCreation(one_group_rect),
            ShowCreation(two_group_rect),
            ShowCreation(three_group_rect),
        )
        self.play(
            Write(one_group_rect_label),
            Write(two_group_rect_label),
            Write(three_group_rect_label),
        )
        self.wait()

        # 定义公式的各部分
        formula_word = (
            Tex("\\log_2{{16}}=\\log_2{2^{{4}}}={{4}}")
            .scale(0.7)
            .set_color_by_tex_to_color_map({"16": RED_A, "4": BLUE_A})
            .next_to(word_line_text_4, DOWN, buff=0.1)
            .align_to(word_line_text_4, LEFT)
        )
        explanation_word = (
            Text("4位<=>16个地址", t2c={"4": BLUE_A, "16": RED_A})
            .next_to(word_line_text_4, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(word_line_text_4, LEFT)
        )

        # 按顺序播放公式的动画
        self.play(Write(formula_word, run_time=3))
        self.wait()
        self.play(ReplacementTransform(formula_word, explanation_word))
        self.wait()

        # 单行四列的表格
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

        # 4位访存计算演示
        bin_expansion_4 = VGroup()
        for i in range(4):
            power_of_two = Tex(f"2^{{ {3-i} }}").scale(0.9)
            times_sign = Tex("\\times")
            bit_val = Text("0").scale(0.9)
            if i != 0:
                plus_sign = Tex("+").next_to(bin_expansion_4, RIGHT, buff=0.1)
                bin_expansion_4.add(plus_sign)

            term = VGroup(power_of_two, times_sign, bit_val)
            term.arrange(RIGHT, buff=0.1)
            term.next_to(bin_expansion_4, RIGHT, buff=0.1)
            bin_expansion_4.add(term)

        bin_expansion_4.scale(0.9).next_to(bit_table_4, DOWN, buff=0.25).shift(
            RIGHT * 1.2
        )
        self.play(Write(bin_expansion_4))
        self.wait()

        for i in range(4):
            # 获取bit_table_4中的位值
            bit_val = bit_table_4[i][1]
            # 动画移动
            self.play(TransformFromCopy(bit_val, bin_expansion_4[2 * i][2]))
            # 更新二进制展开式中对应的值
            new_text = (
                Text(bit_val.text, color=YELLOW)
                .scale(0.8)
                .move_to(bin_expansion_4[2 * i][2].get_center())
            )
            self.play(Transform(bin_expansion_4[2 * i][2], new_text), run_time=0.25)
        self.wait()

        bin_expansion_result_4 = (
            Tex("= 0 + 0 + 0 + 0 = 0")
            .scale(0.8)
            .next_to(bin_expansion_4, DOWN, buff=0.15)
            .align_to(bin_expansion_4, RIGHT)
            .shift(RIGHT * 0.2)
        )
        self.play(Write(bin_expansion_result_4))
        self.wait()

        # 箭头指向第一行
        addressing_arrow_4 = Arrow(
            bin_expansion_result_4.get_right() + RIGHT * 0.1,
            one_group_rect_label.get_left() + LEFT * 0.1,
            buff=0.1,
            stroke_width=2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(addressing_arrow_4))
        self.play(Indicate(one_group_rect))
        self.wait()
        self.play(FadeOut(addressing_arrow_4))
        self.wait()

        # 创建一个新的Text对象，并设置其位置为原始bit_label的位置
        new_bit_4_label_0 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_4[0][1].get_center())
        )
        new_bit_4_label_1 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_4[1][1].get_center())
        )
        new_bit_4_label_2 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_4[2][1].get_center())
        )
        new_bit_4_label_3 = (
            Text("1", color=YELLOW).scale(0.5).move_to(bit_table_4[3][1].get_center())
        )
        self.play(
            ReplacementTransform(bit_table_4[0][1], new_bit_4_label_0),
            ReplacementTransform(bit_table_4[1][1], new_bit_4_label_1),
            ReplacementTransform(bit_table_4[2][1], new_bit_4_label_2),
            ReplacementTransform(bit_table_4[3][1], new_bit_4_label_3),
        )
        self.wait()
        self.play(Indicate(bit_table_4[0:4]))
        self.wait()

        new_4_text_0 = (
            Text(new_bit_4_label_0.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion_4[0][2].get_center())
        )
        self.play(Transform(bin_expansion_4[0][2], new_4_text_0), run_time=0.25)
        self.wait()

        new_4_text_1 = (
            Text(new_bit_4_label_1.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion_4[2][2].get_center())
        )
        self.play(Transform(bin_expansion_4[2][2], new_4_text_1), run_time=0.25)
        self.wait()

        new_4_text_2 = (
            Text(new_bit_4_label_2.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion_4[4][2].get_center())
        )
        self.play(Transform(bin_expansion_4[4][2], new_4_text_2), run_time=0.25)
        self.wait()

        new_4_text_3 = (
            Text(new_bit_4_label_3.text, color=YELLOW)
            .scale(0.8)
            .move_to(bin_expansion_4[6][2].get_center())
        )
        self.play(Transform(bin_expansion_4[6][2], new_4_text_3), run_time=0.25)
        self.wait()
        self.play(
            Indicate(bin_expansion_4[0][2]),
            Indicate(bin_expansion_4[2][2]),
            Indicate(bin_expansion_4[4][2]),
            Indicate(bin_expansion_4[6][2]),
        )
        self.wait()

        bin_expansion_result_4_1 = (
            Tex("= 8 + 4 + 2 + 1 = 15")
            .scale(0.8)
            .next_to(bin_expansion_4, DOWN, buff=0.15)
            .align_to(bin_expansion_4, RIGHT)
            .shift(RIGHT * 0.2)
        )
        self.play(
            ReplacementTransform(bin_expansion_result_4, bin_expansion_result_4_1)
        )
        self.wait()

        addressing_arrow_4 = Arrow(
            bin_expansion_result_4_1.get_right() + RIGHT * 0.1,
            three_group_rect_label.get_left() + LEFT * 0.1,
            buff=0.1,
            stroke_width=2,
            stroke_color=ORANGE,
        )
        self.play(ShowCreation(addressing_arrow_4))
        self.play(Indicate(three_group_rect))
        self.wait()
        self.play(FadeOut(addressing_arrow_4))
        self.play(FadeOut(bin_expansion_result_4_1), FadeOut(bin_expansion_4))
        self.wait()

        # 创建16x4的内存矩形网格
        memory_table = VGroup()
        memory_table_rect = VGroup()
        memory_table_label = VGroup()
        row_labels = VGroup()

        # 添加矩形和标签到相应的VGroup中
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

        # 整合所有部分
        memory_table.add(memory_table_rect, memory_table_label, row_labels)
        memory_table.to_edge(UP, buff=0.5).shift(LEFT * 0.2)
        self.play(
            FadeOut(one_group_rect),
            FadeOut(two_group_rect),
            FadeOut(three_group_rect),
            FadeOut(one_group_rect_label),
            FadeOut(two_group_rect_label),
            FadeOut(three_group_rect_label),
            FadeOut(table),
            FadeOut(bin_dec_table),
        )
        self.play(FadeIn(memory_table))
        self.wait()

        # 修改line_text
        new_byte_line_text = (
            Text("""1"格"(Grid) 为 1字节(Byte)""", color=YELLOW, t2c={"格": RED})
            .scale(0.7)
            .next_to(byte_bit_text, DOWN, buff=0.15)
            .align_to(byte_bit_text, LEFT)
        )
        self.play(TransformMatchingStrings(byte_line_text, new_byte_line_text))
        self.wait()

        new_explanation = (
            Text('6位<=>64个"格"', t2c={"6": BLUE_A, "64": RED_A, "格": RED})
            .next_to(byte_line_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(byte_line_text, LEFT)
        )
        self.play(TransformMatchingShapes(explanation, new_explanation))
        self.wait()

        # 闪烁一格，箭头指向8位的矩形
        grid_arrow = Arrow(
            memory_table_rect[3].get_center() + RIGHT * 0.2,
            memory_table_rect[3].get_center() + RIGHT * 2,
            buff=0.2,
            stroke_color=ORANGE,
        )
        self.play(FlashAround(memory_table_rect[3]))
        self.play(ShowCreation(grid_arrow))

        # 一个矩形指向一个单行八列的表格
        bit_table_8 = VGroup()
        for i in range(8):
            bit_rect = Rectangle(height=0.45, width=0.45)
            if i == 0 or i == 2 or i == 3 or i == 5:
                bit_label = (
                    Text("0", color=YELLOW).scale(0.3).move_to(bit_rect.get_center())
                )
            else:
                bit_label = (
                    Text("1", color=YELLOW).scale(0.3).move_to(bit_rect.get_center())
                )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(grid_arrow, RIGHT)
            else:
                bit.next_to(bit_table_8[-1], RIGHT, buff=0)
            bit_table_8.add(bit)

        self.play(FadeIn(bit_table_8))
        self.wait(2)

        brace_8 = Brace(bit_table_8, DOWN, buff=0.1)
        brace_8_text = (
            brace_8.get_text("8位(bit)", buff=0.1).scale(0.7).set_color(YELLOW)
        )
        self.play(GrowFromCenter(brace_8), Write(brace_8_text))
        self.wait()
        self.play(
            FadeOut(bit_table_8),
            FadeOut(grid_arrow),
            FadeOut(brace_8_text),
            FadeOut(brace_8),
        )
        self.wait()

        new_word_line_text = (
            Text('1"行"(line) 为 1字(Word)', color=YELLOW, t2c={(None, 1): PURPLE_B})
            .scale(0.7)
            .next_to(word_byte_text_4, DOWN, buff=0.15)
            .align_to(word_byte_text_4, LEFT)
        )
        self.play(TransformMatchingStrings(word_line_text_4, new_word_line_text))
        self.wait()

        new_explanation_word = (
            Text('4位<=>16个"行"', t2c={"4": BLUE_A, "16": RED_A, "行": PURPLE_B})
            .next_to(new_word_line_text, DOWN, buff=0.1)
            .scale(0.6)
            .align_to(new_word_line_text, LEFT)
        )
        self.play(TransformMatchingShapes(explanation_word, new_explanation_word))
        self.wait()

        # 箭头
        line_arrow = Arrow(
            memory_table_rect[3].get_center() + RIGHT * 0.2,
            memory_table_rect[3].get_center() + RIGHT * 2,
            buff=0.2,
            stroke_color=ORANGE,
        )
        for i in range(1):
            self.play(FlashAround(memory_table_rect[i * 4 : (i + 1) * 4]))
            self.wait()
        self.play(ShowCreation(line_arrow))

        # 一个矩形指向一个四行八列的表格
        bit_table_32 = VGroup()
        bit_values = {
            (0, 0): "1",
            (0, 3): "1",
            (0, 4): "1",
            (0, 5): "1",
            (0, 6): "1",
            (0, 7): "1",
            (1, 1): "1",
            (1, 2): "1",
            (1, 5): "1",
            (1, 6): "1",
            (2, 1): "1",
            (2, 2): "1",
            (2, 5): "1",
            (2, 6): "1",
            (3, 0): "1",
            (3, 3): "1",
            (3, 5): "1",
            (3, 6): "1",
        }
        for j in range(4):  # 外层循环迭代四行
            for i in range(8):  # 内层循环迭代八列
                bit_rect = Rectangle(height=0.45, width=0.45)
                bit_value = bit_values.get((j, i), "0")
                bit_label = (
                    Text(bit_value, color=YELLOW)
                    .scale(0.3)
                    .move_to(bit_rect.get_center())
                )
                bit = VGroup(bit_rect, bit_label)

                if i == 0 and j == 0:  # 第一行的第一个元素
                    bit.next_to(line_arrow, RIGHT)
                elif i == 0:  # 后续行的第一个元素
                    bit.next_to(bit_table_32[-8], DOWN, buff=0)
                else:  # 其他元素
                    bit.next_to(bit_table_32[-1], RIGHT, buff=0)
                bit_table_32.add(bit)
        self.play(FadeIn(bit_table_32))
        self.wait()

        # 分别右边和下边两个括号
        brace_32 = Brace(bit_table_32, DOWN, buff=0.1)
        brace_32_text = (
            brace_32.get_text("32个位(bit)", buff=0.1).scale(0.7).set_color(YELLOW)
        )
        self.play(GrowFromCenter(brace_32), Write(brace_32_text))
        self.wait()
        self.play(
            FadeOut(bit_table_32),
            FadeOut(line_arrow),
            FadeOut(brace_32_text),
            FadeOut(brace_32),
        )
        self.wait()

        self.play(
            FadeOut(word_byte_text_4),
            FadeOut(new_word_line_text),
            FadeOut(word_addressed_text),
            FadeOut(new_byte_line_text),
            FadeOut(byte_addressed_text),
            FadeOut(memory_size_text),
            FadeOut(byte_bit_text),
        )
        self.wait()

        self.play(Indicate(bit_table_6[4:6]))
        self.wait()
        # 在bit_table_6[4:6]下面添加一个问号
        question_mark = Text("?", color=RED).scale(2).next_to(bit_table_6[4:6], DOWN)
        self.play(Write(question_mark))
        self.wait()

        self.play(
            FadeOut(memory_table),
            FadeOut(new_bit_label_0),
            FadeOut(new_bit_label_1),
            FadeOut(new_bit_label_2),
            FadeOut(new_bit_label_3),
            FadeOut(new_bit_label_5),
            FadeOut(new_bit_4_label_0),
            FadeOut(new_bit_4_label_1),
            FadeOut(new_bit_4_label_2),
            FadeOut(new_bit_4_label_3),
            FadeOut(bit_table_6),
            FadeOut(bit_table_4),
            FadeOut(question_mark),
            FadeOut(new_explanation_word),
            FadeOut(new_explanation),
        )


class Addressing(Scene):
    def construct(self) -> None:
        # 创建文本：内存大小为64B
        memory_size_text = Text("内存大小: 64B").to_edge(UP + LEFT)
        self.play(Write(memory_size_text))
        self.wait()

        # 创建16x4的内存矩形网格
        memory_table = VGroup()
        memory_table_rect = VGroup()
        memory_table_label = VGroup()
        row_labels = VGroup()

        # 添加矩形和标签到相应的VGroup中
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

        # 整合所有部分
        memory_table.add(memory_table_rect, memory_table_label, row_labels)
        memory_table.to_edge(UP, buff=0.5).shift(RIGHT * 0.5)
        self.play(FadeIn(memory_table))
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
            Text("""1"格"(Grid) 为 1字节(Byte)""", color=YELLOW)
            .scale(0.8)
            .next_to(byte_addressed_text, DOWN, buff=0.2)
            .align_to(byte_addressed_text, LEFT)
        )
        self.play(Write(byte_line_text))
        self.wait()

        # 闪烁第一行的四格
        for i in range(4):
            self.play(FlashAround(memory_table_rect[i]))
        self.wait()

        # 定义公式的各部分
        formula = (
            Tex("\\log_2{{64}}=\\log_2{2^{{6}}}={{6}}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"64": RED_A, "6": BLUE_A})
            .next_to(byte_line_text, DOWN, buff=0.2)
            .align_to(byte_line_text, LEFT)
        )
        explanation = (
            Text("6位<=>64格", t2c={"6": BLUE_A, "64": RED_A})
            .next_to(byte_line_text, DOWN, buff=0.1)
            .scale(0.8)
            .align_to(byte_line_text, LEFT)
        )

        # 按顺序播放公式的动画
        self.play(Write(formula, run_time=3))
        self.wait()
        self.play(ReplacementTransform(formula, explanation))
        self.wait()

        # 单行六列的表格
        bit_table_6 = VGroup()
        for i in range(6):
            bit_rect = Rectangle(height=0.7, width=0.7)
            bit_label = (
                Text("0", color=YELLOW).scale(0.6).move_to(bit_rect.get_center())
            )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(explanation, DOWN, buff=0.2)
            else:
                bit.next_to(bit_table_6[-1], RIGHT, buff=0)
            bit_table_6.add(bit)

        bit_table_6.align_to(explanation, LEFT)

        self.play(FadeIn(bit_table_6))
        self.wait(2)

        line_text = (
            Text("""1"行"(Line) 包括 4字节(Byte)""", color=YELLOW)
            .scale(0.8)
            .next_to(bit_table_6, DOWN, buff=1)
            .align_to(bit_table_6, LEFT)
        )
        self.play(Write(line_text))
        self.wait()

        for i in range(4):
            self.play(FlashAround(memory_table_rect[i * 4 : (i + 1) * 4]))
        self.wait()

        # 定义公式的各部分
        formula_row = (
            Tex("\\log_2{{16}}=\\log_2{2^{{4}}}={{4}}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"16": RED_A, "4": BLUE_A})
            .next_to(line_text, DOWN, buff=0.2)
            .align_to(line_text, LEFT)
        )
        explanation_row = (
            Text("4位<=>16行", t2c={"4": BLUE_A, "16": RED_A})
            .next_to(line_text, DOWN, buff=0.1)
            .scale(0.8)
            .align_to(line_text, LEFT)
        )

        # 按顺序播放公式的动画
        self.play(Write(formula_row, run_time=3))
        self.wait()
        self.play(ReplacementTransform(formula_row, explanation_row))
        self.wait()

        # 单行四列的表格
        bit_table_4 = VGroup()
        for i in range(4):
            bit_rect = Rectangle(height=0.7, width=0.7)
            bit_label = (
                Text("0", color=YELLOW).scale(0.6).move_to(bit_rect.get_center())
            )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(explanation_row, DOWN, buff=0.2)
            else:
                bit.next_to(bit_table_4[-1], RIGHT, buff=0)
            bit_table_4.add(bit)

        bit_table_4.align_to(explanation_row, LEFT)

        self.play(FadeIn(bit_table_4))
        self.wait()

        # 定义公式的各部分
        formula_col = (
            Tex("\\log_2{{4}}=\\log_2{2^{{2}}}={{2}}")
            .scale(0.8)
            .set_color_by_tex_to_color_map({"4": RED_A, "2": BLUE_A})
            .next_to(explanation_row, RIGHT, buff=0.6)
        )
        explanation_col = (
            Text("2位<=>4列", t2c={"2": BLUE_A, "4": RED_A})
            .next_to(explanation_row, RIGHT, buff=1)
            .scale(0.8)
        )

        self.play(Indicate(memory_table_rect[0:4]), Indicate(memory_table_label[0:4]))
        self.wait()
        self.play(Write(formula_col, run_time=3))
        self.wait()
        self.play(ReplacementTransform(formula_col, explanation_col))
        self.wait()

        # 单行二列的表格
        bit_table_2 = VGroup()
        for i in range(2):
            bit_rect = Rectangle(height=0.7, width=0.7)
            bit_label = (
                Text("0", color=YELLOW).scale(0.6).move_to(bit_rect.get_center())
            )
            bit = VGroup(bit_rect, bit_label)
            if i == 0:
                bit.next_to(explanation_col, DOWN, buff=0.2)
            else:
                bit.next_to(bit_table_2[-1], RIGHT, buff=0)
            bit_table_2.add(bit)

        bit_table_2.align_to(explanation_col, LEFT)

        self.play(FadeIn(bit_table_2))
        self.wait()

        memory_table.generate_target()
        memory_table.target.to_edge(UP, buff=4.5).shift(RIGHT * 2.2).scale(2)
        self.play(MoveToTarget(memory_table))
        self.wait()

        # 列的00,01,10,11
        col_text_0 = (
            Text("00", color=PURPLE_A)
            .scale(0.7)
            .next_to(memory_table_rect[0], UP, buff=0.2)
            .align_to(memory_table_rect[0], ORIGIN)
        )
        col_text_1 = (
            Text("01", color=PURPLE_A)
            .scale(0.7)
            .next_to(memory_table_rect[1], UP, buff=0.2)
            .align_to(memory_table_rect[1], ORIGIN)
        )
        col_text_2 = (
            Text("10", color=PURPLE_A)
            .scale(0.7)
            .next_to(memory_table_rect[2], UP, buff=0.2)
            .align_to(memory_table_rect[2], ORIGIN)
        )
        col_text_3 = (
            Text("11", color=PURPLE_A)
            .scale(0.7)
            .next_to(memory_table_rect[3], UP, buff=0.2)
            .align_to(memory_table_rect[3], ORIGIN)
        )
        self.play(
            Write(col_text_0), Write(col_text_1), Write(col_text_2), Write(col_text_3)
        )
        self.wait()

        # 6位表格的箭头和计算结果
        bit_table_6_arrow = Arrow(
            bit_table_6.get_right(),
            bit_table_6.get_right() + RIGHT * 1.2,
            buff=0.2,
            stroke_color=ORANGE,
        )
        bit_table_6_result = (
            Text("0", color=BLUE_C)
            .scale(0.8)
            .next_to(bit_table_6_arrow, RIGHT, buff=0.2)
        )
        bit_table_6_result_arrow = CurvedArrow(
            start_point=bit_table_6_result.get_right() + RIGHT * 0.2,
            end_point=memory_table_rect[0].get_center() + LEFT * 0.2,
            angle=-TAU / 4,
            color=GREEN,
        )
        self.play(Indicate(bit_table_6))
        self.play(ShowCreation(bit_table_6_arrow))
        self.wait()
        self.play(Write(bit_table_6_result))
        self.wait()
        self.play(ShowCreation(bit_table_6_result_arrow))
        self.play(FlashAround(memory_table_rect[0]), Indicate(memory_table_label[0]))
        self.play(FadeOut(bit_table_6_result_arrow))
        self.wait()

        # 4位表格的箭头和2位表格的箭头和计算结果
        bit_table_4_arrow = Arrow(
            bit_table_4.get_bottom(),
            bit_table_4.get_bottom() + DOWN * 1,
            buff=0.2,
            stroke_color=ORANGE,
        )
        bit_table_4_result = (
            Text("0", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_4_arrow, DOWN, buff=0.2)
        )
        bit_table_4_result_arrow = CurvedArrow(
            start_point=bit_table_4_result.get_bottom() + DOWN * 0.2,
            end_point=row_labels[0].get_left() + LEFT * 0.2,
            angle=TAU / 4,
            color=GREEN,
        )
        bit_table_2_arrow = CurvedArrow(
            start_point=bit_table_2.get_right() + RIGHT * 0.2,
            end_point=col_text_0.get_left() + LEFT * 0.2,
            angle=-TAU / 6,
            color=GREEN,
        )
        self.play(Indicate(bit_table_4))
        self.play(ShowCreation(bit_table_4_arrow))
        self.wait()
        self.play(Write(bit_table_4_result))
        self.wait()
        self.play(ShowCreation(bit_table_4_result_arrow))
        self.play(FlashAround(memory_table_rect[0:4]), Indicate(row_labels[0]))
        self.play(FadeOut(bit_table_4_result_arrow))
        self.wait()
        self.play(Indicate(bit_table_2))
        self.wait()
        self.play(ShowCreation(bit_table_2_arrow))
        self.play(Indicate(col_text_0))
        self.play(FadeOut(bit_table_2_arrow))
        self.wait()
        self.play(FlashAround(memory_table_rect[0]), Indicate(memory_table_label[0]))
        self.wait()

        # 更新结果
        bit_6_label_1 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_6[5][1].get_center())
        )
        self.play(Transform(bit_table_6[5][1], bit_6_label_1))
        self.wait()
        self.play(Indicate(bit_table_6))
        self.wait()

        bit_table_6_result_1 = (
            Text("1", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_6_arrow, RIGHT, buff=0.2)
        )
        bit_table_6_result_arrow_1 = CurvedArrow(
            start_point=bit_table_6_result_1.get_right() + RIGHT * 0.2,
            end_point=memory_table_rect[1].get_center() + LEFT * 0.2,
            angle=-TAU / 4,
            color=GREEN,
        )
        self.play(Transform(bit_table_6_result, bit_table_6_result_1))
        self.wait()
        self.play(ShowCreation(bit_table_6_result_arrow_1))
        self.play(FlashAround(memory_table_rect[1]), Indicate(memory_table_label[1]))
        self.play(FadeOut(bit_table_6_result_arrow_1))
        self.wait()

        bit_2_label_1 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_2[1][1].get_center())
        )
        bit_table_2_arrow_1 = CurvedArrow(
            start_point=bit_table_2.get_right() + RIGHT * 0.2,
            end_point=col_text_1.get_left() + LEFT * 0.2,
            angle=-TAU / 6,
            color=GREEN,
        )
        self.play(Indicate(bit_table_4))
        self.wait()
        self.play(ShowCreation(bit_table_4_result_arrow))
        self.play(FlashAround(memory_table_rect[0:4]), Indicate(row_labels[0]))
        self.play(FadeOut(bit_table_4_result_arrow))
        self.wait()
        self.play(Transform(bit_table_2[1][1], bit_2_label_1))
        self.wait()
        self.play(Indicate(bit_table_2))
        self.wait()
        self.play(ShowCreation(bit_table_2_arrow_1))
        self.play(Indicate(col_text_1))
        self.play(FadeOut(bit_table_2_arrow_1))
        self.wait()
        self.play(FlashAround(memory_table_rect[1]), Indicate(memory_table_label[1]))
        self.wait()

        # 更新结果
        bit_6_label_2 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_6[4][1].get_center())
        )
        self.play(Transform(bit_table_6[4][1], bit_6_label_2))
        self.wait()
        self.play(Indicate(bit_table_6))
        self.wait()

        bit_table_6_result_2 = (
            Text("3", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_6_arrow, RIGHT, buff=0.2)
        )
        bit_table_6_result_arrow_2 = CurvedArrow(
            start_point=bit_table_6_result_2.get_right() + RIGHT * 0.2,
            end_point=memory_table_rect[3].get_center() + LEFT * 0.2,
            angle=-TAU / 4,
            color=GREEN,
        )
        self.play(Transform(bit_table_6_result, bit_table_6_result_2))
        self.wait()
        self.play(ShowCreation(bit_table_6_result_arrow_2))
        self.play(FlashAround(memory_table_rect[3]), Indicate(memory_table_label[3]))
        self.play(FadeOut(bit_table_6_result_arrow_2))
        self.wait()

        bit_2_label_2 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_2[0][1].get_center())
        )
        bit_table_2_arrow_2 = CurvedArrow(
            start_point=bit_table_2.get_right() + RIGHT * 0.2,
            end_point=col_text_3.get_left() + LEFT * 0.2,
            angle=-TAU / 6,
            color=GREEN,
        )
        self.play(Indicate(bit_table_4))
        self.wait()
        self.play(ShowCreation(bit_table_4_result_arrow))
        self.play(FlashAround(memory_table_rect[0:4]), Indicate(row_labels[0]))
        self.play(FadeOut(bit_table_4_result_arrow))
        self.wait()
        self.play(Transform(bit_table_2[0][1], bit_2_label_2))
        self.wait()
        self.play(Indicate(bit_table_2))
        self.wait()
        self.play(ShowCreation(bit_table_2_arrow_2))
        self.play(Indicate(col_text_3))
        self.play(FadeOut(bit_table_2_arrow_2))
        self.wait()
        self.play(FlashAround(memory_table_rect[3]), Indicate(memory_table_label[3]))
        self.wait()

        # 更新结果
        bit_6_label_3 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_6[3][1].get_center())
        )
        self.play(Transform(bit_table_6[3][1], bit_6_label_3))
        self.wait()
        self.play(Indicate(bit_table_6))
        self.wait()

        bit_table_6_result_3 = (
            Text("7", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_6_arrow, RIGHT, buff=0.2)
        )
        bit_table_6_result_arrow_3 = CurvedArrow(
            start_point=bit_table_6_result_3.get_right() + RIGHT * 0.2,
            end_point=memory_table_rect[7].get_center() + LEFT * 0.2,
            angle=-TAU / 4,
            color=GREEN,
        )
        self.play(Transform(bit_table_6_result, bit_table_6_result_3))
        self.wait()
        self.play(ShowCreation(bit_table_6_result_arrow_3))
        self.play(FlashAround(memory_table_rect[7]), Indicate(memory_table_label[7]))
        self.play(FadeOut(bit_table_6_result_arrow_3))
        self.wait()

        bit_4_label_3 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_4[3][1].get_center())
        )
        self.play(Transform(bit_table_4[3][1], bit_4_label_3))
        self.wait()
        self.play(Indicate(bit_table_4))
        self.wait()

        bit_table_4_result_3 = (
            Text("1", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_4_arrow, DOWN, buff=0.2)
        )
        bit_table_4_result_arrow_3 = CurvedArrow(
            start_point=bit_table_4_result_3.get_bottom() + DOWN * 0.2,
            end_point=row_labels[1].get_left() + LEFT * 0.2,
            angle=TAU / 4,
            color=GREEN,
        )
        self.play(Transform(bit_table_4_result, bit_table_4_result_3))
        self.wait()
        self.play(ShowCreation(bit_table_4_result_arrow_3))
        self.play(FlashAround(memory_table_rect[4:8]), Indicate(row_labels[1]))
        self.play(FadeOut(bit_table_4_result_arrow_3))
        self.wait()
        self.play(Indicate(bit_table_2))
        self.wait()
        self.play(ShowCreation(bit_table_2_arrow_2))
        self.play(Indicate(col_text_3))
        self.play(FadeOut(bit_table_2_arrow_2))
        self.wait()
        self.play(FlashAround(memory_table_rect[7]), Indicate(memory_table_label[7]))
        self.wait(2)

        # 更新结果
        bit_table_6_result_4 = (
            Text("25", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_6_arrow, RIGHT, buff=0.2)
        )
        bit_table_6_result_arrow_4 = CurvedArrow(
            start_point=memory_table_rect[25].get_center() + LEFT * 0.2,
            end_point=bit_table_6_result_4.get_right() + RIGHT * 0.2,
            angle=-TAU / 4,
            color=GREEN,
        )
        self.play(FlashAround(memory_table_rect[25]), Indicate(memory_table_label[25]))
        self.wait()
        self.play(ShowCreation(bit_table_6_result_arrow_4))
        self.play(Transform(bit_table_6_result, bit_table_6_result_4))
        self.play(FadeOut(bit_table_6_result_arrow_4))
        self.wait()

        bit_table_6_arrow_reverse = Arrow(
            bit_table_6.get_right() + RIGHT * 1.2,
            bit_table_6.get_right(),
            buff=0.2,
            stroke_color=ORANGE,
        )
        self.play(Transform(bit_table_6_arrow, bit_table_6_arrow_reverse))
        self.wait()

        bit_6_label_40 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_6[1][1].get_center())
        )
        bit_6_label_41 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_6[2][1].get_center())
        )
        bit_6_label_42 = (
            Text("0", color=YELLOW).scale(0.6).move_to(bit_6_label_3.get_center())
        )
        bit_6_label_43 = (
            Text("0", color=YELLOW).scale(0.6).move_to(bit_6_label_2.get_center())
        )
        self.play(
            Transform(bit_table_6[1][1], bit_6_label_40),
            Transform(bit_table_6[2][1], bit_6_label_41),
            Transform(bit_table_6[3][1], bit_6_label_42),
            Transform(bit_table_6[4][1], bit_6_label_43),
        )
        self.wait()
        self.play(Indicate(bit_table_6))
        self.wait()

        bit_4_label_40 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_4[1][1].get_center())
        )
        bit_4_label_41 = (
            Text("1", color=YELLOW).scale(0.6).move_to(bit_table_4[2][1].get_center())
        )
        bit_4_label_42 = (
            Text("0", color=YELLOW).scale(0.6).move_to(bit_table_4[3][1].get_center())
        )
        bit_table_4_result_4 = (
            Text("6", color=BLUE_D)
            .scale(0.8)
            .next_to(bit_table_4_arrow, DOWN, buff=0.2)
        )
        bit_table_4_result_arrow_4 = CurvedArrow(
            start_point=bit_table_4_result_4.get_right() + RIGHT * 0.2,
            end_point=row_labels[6].get_left() + LEFT * 0.2,
            angle=0,
            color=GREEN,
        )
        self.play(
            Transform(bit_table_4[1][1], bit_4_label_40),
            Transform(bit_table_4[2][1], bit_4_label_41),
            Transform(bit_table_4[3][1], bit_4_label_42),
        )
        self.wait()
        self.play(Indicate(bit_table_4))
        self.wait()
        self.play(Transform(bit_table_4_result, bit_table_4_result_4))
        self.wait()
        self.play(ShowCreation(bit_table_4_result_arrow_4))
        self.play(FlashAround(memory_table_rect[24:28]), Indicate(row_labels[6]))
        self.play(FadeOut(bit_table_4_result_arrow_4))
        self.wait()

        bit_2_label_4 = (
            Text("0", color=YELLOW).scale(0.6).move_to(bit_table_2[0][1].get_center())
        )
        bit_table_2_arrow_4 = CurvedArrow(
            start_point=bit_table_2.get_right() + RIGHT * 0.2,
            end_point=col_text_1.get_left() + LEFT * 0.2,
            angle=-TAU / 6,
            color=GREEN,
        )
        self.play(
            Transform(bit_table_2[0][1], bit_2_label_4),
        )
        self.wait()
        self.play(Indicate(bit_table_2))
        self.wait()
        self.play(ShowCreation(bit_table_2_arrow_4))
        self.play(Indicate(col_text_1))
        self.play(FadeOut(bit_table_2_arrow_4))
        self.wait()
        self.play(FlashAround(memory_table_rect[25]), Indicate(memory_table_label[25]))
        self.wait(2)

        # 全部清空
        self.clear()


class Ending(Scene):
    def construct(self) -> None:
        # 直接映射
        label_1 = (
            Text("直接映射(Direct Memory Mapping)", color=PURPLE_B)
            .scale(0.8)
            .to_edge(UP, buff=0.2)
        )
        rect_t_1 = (
            Rectangle(height=0.7, width=2.5, color=BLUE)
            .next_to(label_1, DOWN)
            .align_to(label_1, LEFT)
        )
        rect_i_1 = Rectangle(height=0.7, width=2, color=GREEN).next_to(
            rect_t_1, RIGHT, buff=0
        )
        rect_o_1 = Rectangle(height=0.7, width=2.5, color=YELLOW).next_to(
            rect_i_1, RIGHT, buff=0
        )

        text_t_1 = (
            Text("标记(Tag)", color=WHITE).scale(0.5).move_to(rect_t_1.get_center())
        )
        text_i_1 = (
            Text("行索引(Index)", color=WHITE).scale(0.5).move_to(rect_i_1.get_center())
        )
        text_o_1 = (
            Text("块内地址(Offset)", color=WHITE).scale(0.5).move_to(rect_o_1.get_center())
        )

        table_1 = VGroup(rect_t_1, rect_i_1, rect_o_1, text_t_1, text_i_1, text_o_1)
        complete_table_1 = VGroup(table_1, label_1)

        self.play(ShowCreation(table_1), Write(label_1))
        self.wait()

        # 全相联映射
        label_2 = (
            Text("全相联映射(Associative Mapping)", color=PURPLE_B)
            .scale(0.8)
            .next_to(complete_table_1, DOWN, buff=0.5)
            .align_to(complete_table_1, LEFT)
        )
        rect_t_2 = (
            Rectangle(height=0.7, width=4, color=BLUE)
            .next_to(label_2, DOWN, buff=0.2)
            .align_to(label_2, LEFT)
        )
        rect_o_2 = Rectangle(height=0.7, width=3, color=YELLOW).next_to(
            rect_t_2, RIGHT, buff=0
        )

        text_t_2 = (
            Text("标记(Tag)", color=WHITE).scale(0.5).move_to(rect_t_2.get_center())
        )
        text_o_2 = (
            Text("块内地址(Offset)", color=WHITE).scale(0.5).move_to(rect_o_2.get_center())
        )

        table_2 = VGroup(rect_t_2, rect_o_2, text_t_2, text_o_2)
        complete_table_2 = VGroup(table_2, label_2)

        self.play(ShowCreation(table_2), Write(label_2))
        self.wait()

        # 组相联映射
        label_3 = (
            Text("组相联映射(Set Associative Mapping)", color=PURPLE_B)
            .scale(0.8)
            .next_to(complete_table_2, DOWN, buff=0.5)
            .align_to(complete_table_2, LEFT)
        )
        rect_t_3 = (
            Rectangle(height=0.7, width=2.2, color=BLUE)
            .next_to(label_3, DOWN, buff=0.2)
            .align_to(label_3, LEFT)
        )
        rect_i_3 = Rectangle(height=0.7, width=2.3, color=GREEN).next_to(
            rect_t_3, RIGHT, buff=0
        )
        rect_o_3 = Rectangle(height=0.7, width=2.5, color=YELLOW).next_to(
            rect_i_3, RIGHT, buff=0
        )

        text_t_3 = (
            Text("标记(Tag)", color=WHITE).scale(0.5).move_to(rect_t_3.get_center())
        )
        text_i_3 = (
            Text("组索引(Set Index)", color=WHITE)
            .scale(0.5)
            .move_to(rect_i_3.get_center())
        )
        text_o_3 = (
            Text("块内地址(Offset)", color=WHITE).scale(0.5).move_to(rect_o_3.get_center())
        )

        table_3 = VGroup(rect_t_3, rect_i_3, rect_o_3, text_t_3, text_i_3, text_o_3)
        complete_table_3 = VGroup(table_3, label_3)

        self.play(ShowCreation(table_3), Write(label_3))
        self.wait()

        # 创建一个大括号，放在table的右侧
        cache_table = VGroup(complete_table_1, complete_table_2, complete_table_3)
        brace = Brace(cache_table, LEFT)
        # 如果你还想添加一个标签或文字在大括号旁边
        brace_label = brace.get_text("Cache映射方式").shift(LEFT * 0.1)
        # 显示在场景中
        self.play(FadeIn(brace))
        self.wait()
        self.play(Write(brace_label))
        self.wait()
        self.play(FadeOut(brace), FadeOut(brace_label))

        # 32位虚拟地址
        label_4 = (
            Text("32位虚拟地址(Virtual Address)", color=PURPLE_B)
            .scale(0.8)
            .next_to(complete_table_3, DOWN, buff=0.5)
            .align_to(complete_table_3, LEFT)
        )
        rect_t_4 = (
            Rectangle(height=0.7, width=2.2, color=BLUE)
            .next_to(label_4, DOWN)
            .align_to(label_4, LEFT)
        )
        rect_i_4 = Rectangle(height=0.7, width=2.2, color=GREEN).next_to(
            rect_t_4, RIGHT, buff=0
        )
        rect_o_4 = Rectangle(height=0.7, width=2.6, color=YELLOW).next_to(
            rect_i_4, RIGHT, buff=0
        )

        text_t_4 = Text("页目录项", color=WHITE).scale(0.5).move_to(rect_t_4.get_center())
        text_i_4 = Text("行索引", color=WHITE).scale(0.5).move_to(rect_i_4.get_center())
        text_o_4 = Text("块内地址", color=WHITE).scale(0.5).move_to(rect_o_4.get_center())

        table_4 = VGroup(rect_t_4, rect_i_4, rect_o_4, text_t_4, text_i_4, text_o_4)
        complete_table_4 = VGroup(table_4, label_4)

        self.play(ShowCreation(table_4), Write(label_4))
        self.wait()

        # 所有的complete_table变为一句话
        complete_table = VGroup(
            complete_table_1, complete_table_2, complete_table_3, complete_table_4
        )
        self.play(FadeOut(complete_table))
        saying = Text("The medium is the message.", color=WHITE).move_to(ORIGIN)
        saying_author = (
            Text("—— Marshall McLuhan", color=WHITE)
            .next_to(saying, DOWN, buff=0.4)
            .shift(RIGHT * 4)
        )
        self.play(Write(saying))
        self.wait()
        self.play(Write(saying_author))
        self.wait()
        self.play(FadeOut(saying), FadeOut(saying_author))


class Cover(Scene):
    def construct(self) -> None:
        # 创建最简单的内存模型
        simple_table = VGroup()
        simple_table_rect = VGroup()
        simple_table_label = VGroup()
        simple_table.add(simple_table_rect)
        simple_table.add(simple_table_label)
        for i in range(8):
            rect = Rectangle(height=0.8, width=2)
            rect.shift(UP * i * 0.8)
            # 然后，定义标签的最终位置（矩形内部的右下角）
            label = Text(str(i), font_size=15, color=BLUE).scale(2)
            simple_table_rect.add(rect)
            simple_table_label.add(label)

        simple_table_rect.arrange(DOWN, aligned_edge=LEFT, buff=0)
        simple_table_rect.scale(1.2).move_to(RIGHT).shift(RIGHT * 3.2)

        # 在排列完矩形后，更新标签的位置
        for i, label in enumerate(simple_table_label):
            label.next_to(simple_table_rect[i], LEFT)

        self.add(simple_table_rect)
        self.wait(1)

        for label in simple_table_label:
            self.add(label)

        self.wait(1)

        # 更新标签的位置
        for i, label in enumerate(simple_table_label):
            target_position = (
                simple_table_rect[i].get_corner(DOWN + RIGHT) + UP * 0.2 + LEFT * 0.2
            )
            self.play(label.animate.move_to(target_position), run_time=0.3)

        title = (
            Text("理解物理内存", color=YELLOW)
            .scale(2.8)
            .to_edge(UL, buff=0.8)
            .shift(RIGHT * 0.2)
        )

        self.add(title)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = f"manimgl {module_name} Cover -s -ow"
    # command = f"manimgl {module_name} Ending -ow"
    os.system(command)
