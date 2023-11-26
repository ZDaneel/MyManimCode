from manimlib import *
import numpy as np

img_path = "./images/npd/"
svg_path = "./images/svg/"


class Warning(Scene):
    def construct(self):
        # Trigger Warning part
        warning_label = Text(
            "Trigger Warning: 包含对精神创伤、虐待、权力控制等行为的描述",
            font_size=45,
            t2c={"Trigger Warning:": RED},
        )
        self.play(Write(warning_label), run_time=3)
        self.wait(2)
        warning_label.generate_target()
        warning_label.target.shift(UP * 2)
        self.play(MoveToTarget(warning_label))
        self.wait(2)

        # Other reminders part
        reminder_label = Text("请记住：", color=YELLOW, font_size=45)
        reminder_label.next_to(
            warning_label.target,
            direction=DOWN,
            buff=MED_LARGE_BUFF * 1.5,
            aligned_edge=LEFT,
        ).shift(RIGHT * 2.2)

        # List items
        list_items = ["科普自恋型虐待", "不要简单对号入座或者贴标签", "如有问题请寻求专业人士的帮助"]

        reminder_list = VGroup()
        for item_text in list_items:
            dot = Dot(radius=0.07, color=YELLOW)
            item = Text(item_text, font_size=40)
            item.next_to(dot, direction=RIGHT, buff=MED_SMALL_BUFF)
            group = VGroup(dot, item)
            reminder_list.add(group)

        reminder_list.arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        reminder_list.next_to(reminder_label, direction=DR, buff=MED_SMALL_BUFF)

        self.play(Write(reminder_label))
        self.wait()
        for reminder in reminder_list:
            self.play(Write(reminder))
            self.wait()
        self.wait(4)
        self.play(
            FadeOut(reminder_label), FadeOut(reminder_list), FadeOut(warning_label)
        )


class Intro(Scene):
    def construct(self) -> None:
        # 导入图片
        person_in_room = (
            ImageMobject(img_path + "person_in_room.png").scale(1.2).shift(UP * 0.5)
        )
        person_in_public = (
            ImageMobject(img_path + "person_in_public.png").scale(1.2).shift(UP * 0.5)
        )
        person_in_bed = (
            ImageMobject(img_path + "person_in_bed.png").scale(1.2).shift(UP * 0.5)
        )

        # 配置文字
        apologize_text = Text("频繁道歉？").set_color(WHITE)
        anxious_text = Text("焦虑？心神不宁？").set_color(WHITE)
        doubt_text = Text("自我怀疑？悲伤？压抑？").set_color(WHITE)
        title_text = Text("自恋型虐待").set_color(WHITE).scale(1.5)

        # 将文字与图片关联
        apologize_text.next_to(person_in_room, DOWN, buff=0.5)
        anxious_text.next_to(person_in_public, DOWN, buff=0.5)
        doubt_text.next_to(person_in_bed, DOWN, buff=0.5)

        # 添加到场景并播放
        self.play(FadeIn(person_in_room), Write(apologize_text))
        self.wait()
        self.play(FadeOut(person_in_room))
        apologize_text.generate_target()
        apologize_text.target.to_edge(UL).shift(DOWN * 2 + RIGHT * 0.5)
        self.play(MoveToTarget(apologize_text))
        self.wait()
        self.play(FadeIn(person_in_public), Write(anxious_text))
        self.wait()
        self.play(FadeOut(person_in_public))
        anxious_text.generate_target()
        anxious_text.target.next_to(apologize_text.target, DOWN, buff=0.5).align_to(
            apologize_text.target, LEFT
        )
        self.play(MoveToTarget(anxious_text))
        self.wait()
        self.play(FadeIn(person_in_bed), Write(doubt_text))
        self.wait()
        self.play(FadeOut(person_in_bed))
        doubt_text.generate_target()
        doubt_text.target.next_to(anxious_text.target, DOWN, buff=0.5).align_to(
            anxious_text.target, LEFT
        )
        self.play(MoveToTarget(doubt_text))
        self.wait()
        question_group = VGroup(apologize_text, anxious_text, doubt_text)
        self.play(ReplacementTransform(question_group, title_text), run_time=2)
        self.wait()

        self.play(FadeOut(title_text[2:]))
        self.wait()

        self.play(
            title_text[0:2].animate.scale(0.6).to_edge(UP).shift(RIGHT * 1.1 + UP * 0.2)
        )
        self.wait()
        up_line = Line(LEFT, RIGHT).scale(5).next_to(title_text[0:2], DOWN, buff=0.15)
        self.play(ShowCreation(up_line))
        self.wait()

        spectrum = Line().scale(4.53).shift(DOWN * 1.35)
        spectrum.set_color_by_gradient(BLUE, RED)

        axes = Axes(
            x_range=[-2.5, 2.5, 0.5],
            y_range=[0, 1.5],
            axis_config={"color": BLUE, "include_ticks": False},
            y_axis_config={
                "include_tip": True,
                "tip_config": {"width": 0.1, "length": 0.3},
            },
        ).scale(1.8)

        axe_labels = [
            AxesLabel(axes, -2.2, "低自恋"),
            AxesLabel(axes, 0, "健康自恋"),
            AxesLabel(axes, 2.2, "病态自恋"),
        ]

        normal_curve_1 = axes.get_graph(
            lambda x: 2
            * (1 / (1 * np.sqrt(2 * np.pi)))
            * np.exp(-(x**2) / (2 * 1**2)),
            color=GREEN_B,
            stroke_width=2,
        )

        normal_curve_2 = axes.get_graph(
            lambda x: 2
            * (1 / (1 * np.sqrt(2 * np.pi)))
            * np.exp(-((x + 0.5) ** 2) / (2 * 1**2)),
            color=YELLOW_B,
            stroke_width=2,
        )
        self.play(ShowCreation(spectrum))
        self.wait()
        self.play(Write(axe_labels[0]))
        self.play(Write(axe_labels[2]))
        self.play(Write(axe_labels[1]))
        self.wait()
        self.play(ShowCreation(normal_curve_1), run_time=2)
        self.wait()

        x_vals_fill = np.linspace(-0.5, 0.5, 100)
        y_vals_fill = (
            2
            * (1 / (1 * np.sqrt(2 * np.pi)))
            * np.exp(-(x_vals_fill**2) / (2 * 1**2))
        )
        fill_coords = [(x, y) for x, y in zip(x_vals_fill, y_vals_fill)]
        fill_coords += [(0.5, 0), (-0.5, 0)]
        filled_area = Polygon(
            *[axes.c2p(x, y) for x, y in fill_coords],
            fill_color=YELLOW_C,
            fill_opacity=0.5,
        )
        self.play(FadeIn(filled_area))
        self.wait()
        self.play(FadeOut(filled_area))

        # self.play(ShowCreation(normal_curve_2), run_time=2)
        self.play(ReplacementTransform(normal_curve_1, normal_curve_2), run_time=2)
        self.wait(2)
        self.play(
            # FadeOut(normal_curve_1),
            FadeOut(normal_curve_2),
            FadeOut(spectrum),
            *[FadeOut(axe_label) for axe_label in axe_labels],
        )

        npd_title = Text("NPD: 自恋型人格障碍", color=RED_C).scale(0.8)
        npd_title.to_edge(UL).shift(DOWN * 0.75)
        dsm_standard = Text(
            """
                            根据精神障碍诊断与统计手册(DSM-5)
                            成年人满足下列五项或更多
                            """
        ).scale(0.6)
        dsm_standard.next_to(npd_title, DOWN).to_edge(LEFT, buff=1)
        alert_text = Text("与原文并不完全一致", color=ORANGE).scale(0.3)
        alert_text.next_to(dsm_standard, DOWN, buff=0.13).align_to(dsm_standard, ORIGIN)

        items = [
            "有一种夸大的自我意识",
            "痴迷于无限成功、权力、才华或理想爱情",
            "认为自己“特殊”和独特",
            "需要过度的钦佩",
            "过分期望特别有利的待遇",
            "利用他人来达到自己的目的",
            "不愿承认或认同他人的感受和需要",
            "经常嫉妒别人",
            "表现出傲慢、傲慢的行为和态度",
        ]

        # 为每个条目添加点并组成VGroup
        item_group = VGroup()
        for item in items:
            dot = Dot().scale(0.5)
            text_item = Text(item).scale(0.5).next_to(dot, RIGHT, buff=0.3)
            line = VGroup(dot, text_item)
            item_group.add(line)

        item_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        item_group.next_to(dsm_standard, DOWN).to_edge(LEFT, buff=1.2).shift(DOWN * 0.2)

        content_rect = SurroundingRectangle(item_group, buff=0.14, stroke_width=1.5)

        self.play(Write(npd_title))
        self.wait()
        self.play(Write(dsm_standard))
        self.wait()
        self.play(Write(alert_text))
        self.play(Write(item_group), DrawBorderThenFill(content_rect), run_time=3)
        self.wait()

        cnpd_title = Text("隐性自恋型人格障碍", color=RED).scale(0.8)
        cnpd_title.next_to(item_group, DOWN, buff=0.4).align_to(item_group, LEFT).shift(
            LEFT * 0.6
        )
        self.play(Write(cnpd_title))
        self.wait()
        exclamation_mark = Text("!!!", color=RED).scale(1.5)
        exclamation_mark.next_to(cnpd_title, RIGHT, buff=0.2)
        self.play(Write(exclamation_mark))
        self.wait()

        # 中间竖线
        divider = Line(UP * 2.2, DOWN * 2.5)
        self.play(ShowCreation(divider))
        self.wait(2)

        # 右侧
        target_title = Text("""受害者体质""", color=BLUE_C).scale(0.8)
        target_title.to_edge(UP).shift(DOWN * 0.75 + RIGHT * 1.8)

        main_points = [
            "低自尊",
            "高同理心",
            "边界感低",
        ]

        sub_points = [
            ["害怕被抛弃", "承担更多不属于自己的责任"],
            ["拯救者的心态", "更容易被病态自恋者负面情绪影响"],
            ["害怕发生对立或冲突", "忽视自己的感受和需求"],
        ]

        main_group = VGroup()
        for idx, point in enumerate(main_points):
            dot = Dot().scale(0.6)
            main_text = Text(point).scale(0.6).next_to(dot, RIGHT, buff=0.2)
            main_line = VGroup(dot, main_text)

            sub_group = VGroup()
            for sub_point in sub_points[idx]:
                sub_dot = Dot().scale(0.5)
                sub_text = Text(sub_point).scale(0.5).next_to(sub_dot, RIGHT, buff=0.2)
                sub_line = VGroup(sub_dot, sub_text)
                sub_group.add(sub_line)

            sub_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            sub_group.next_to(main_line, DOWN).align_to(main_line, LEFT).shift(
                RIGHT * 0.5
            )

            line_group = VGroup(main_line, sub_group)
            main_group.add(line_group)

        main_group.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        main_group.next_to(target_title, DOWN, buff=0.5).align_to(
            target_title, LEFT
        ).shift(RIGHT * 0.5)

        self.play(Write(target_title))
        # self.play(Write(main_group))
        for line_group in main_group:
            self.play(Write(line_group[0]))
            self.wait()
            self.play(Write(line_group[1]))
            self.wait()
        self.wait(3)

        self.play(
            FadeOut(VGroup(npd_title, dsm_standard, alert_text)),
            FadeOut(divider),
            FadeOut(cnpd_title),
            FadeOut(exclamation_mark),
            FadeOut(item_group),
            FadeOut(content_rect),
            FadeOut(target_title),
            FadeOut(main_group),
            FadeOut(up_line),
            FadeOut(title_text[0:2]),
        )


class Abuse(Scene):
    def construct(self) -> None:
        abuse_title = Text("虐待").scale(0.9).to_edge(UP)
        up_line = Line(LEFT, RIGHT).scale(5).next_to(abuse_title, DOWN, buff=0.15)
        self.play(Write(abuse_title))
        self.play(ShowCreation(up_line))
        self.wait()

        physical_abuse = Text("身体层面", color=RED).scale(0.8)
        mental_abuse = Text("心理层面", color=RED).scale(0.8)
        physical_abuse.next_to(up_line, DOWN, buff=0.5).align_to(up_line, ORIGIN)
        mental_abuse.next_to(up_line, DOWN, buff=0.5).align_to(up_line, ORIGIN)
        self.play(Write(physical_abuse))
        self.wait()
        physical_img = ImageMobject(img_path + "physical_abuse.png").scale(1.2)
        physical_img.next_to(physical_abuse, DOWN, buff=0.25).align_to(
            physical_abuse, ORIGIN
        )
        self.play(FadeIn(physical_img))
        self.wait()
        self.play(FadeOut(physical_img))
        self.wait()
        self.play(TransformMatchingStrings(physical_abuse, mental_abuse))
        self.wait()
        self.play(FadeOut(mental_abuse))
        self.wait()

        terms = ["煤气灯", "贬低", "情感勒索", "利用他人", "抛弃", "纠缠不清"]

        descriptions = [
            "否定事实或你的感受",
            "批评、泼冷水",
            "FOG-恐惧、义务和内疚",
            "孤立受害者或利用第三者",
            "冷暴力、断崖式分手",
            "病态的和解，为了回吸",
        ]

        term_texts = VGroup(*[Text(term, color=RED_D).scale(0.8) for term in terms])
        desc_texts = VGroup(
            *[Text(desc, font_size=30).scale(0.7) for desc in descriptions]
        )

        term_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        desc_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.7)

        lines = VGroup()
        line_0 = Line(LEFT, RIGHT, stroke_width=2).set_width(FRAME_WIDTH - 6)
        lines.add(line_0)
        for i in range(1, len(term_texts)):
            new_line = line_0.copy()
            lines.add(new_line)
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        ellipsis_text = (
            Text("...", color=RED_D)
            .scale(1.8)
            .next_to(lines[-1], DOWN, buff=0.5)
            .shift(LEFT * 2.2)
        )
        vertical_line = Line(UP * 1.8, DOWN * 3, color=WHITE, stroke_width=2).move_to(
            ORIGIN
        )

        for term, desc, line in zip(term_texts, desc_texts, lines):
            term.next_to(line, UL, buff=0.15).align_to(line, LEFT).shift(RIGHT * 1.6)
            desc.next_to(term, RIGHT).align_to(line.end, LEFT)

        self.play(ShowCreation(vertical_line))
        for term, desc, line in zip(term_texts, desc_texts, lines):
            self.play(Write(term))
            self.play(Write(desc))
            self.wait()
            self.play(ShowCreation(line))
            self.wait()
        self.play(Write(ellipsis_text))
        self.wait()

        self.play(
            FadeOut(VGroup(abuse_title, up_line, vertical_line, ellipsis_text)),
            FadeOut(term_texts),
            FadeOut(desc_texts),
            FadeOut(lines),
        )


class Respond(Scene):
    def construct(self):
        center_circle = Circle(radius=1, stroke_color=WHITE)
        center_text = (
            Text(
                """
                           相信自己的
                           感受和直觉""",
                t2c={"感受": BLUE_C, "直觉": YELLOW_B},
            )
            .scale(0.6)
            .move_to(center_circle.get_center())
        )

        circle0 = (
            Rectangle(stroke_color=WHITE)
            .scale(0.5)
            .next_to(center_circle, direction=RIGHT, buff=2.5)
        )
        text0 = (
            Text(
                """
                    放弃拯救幻想
                    尽可能远离 
                    """,
                t2c={"放弃拯救": RED_C, "远离": PURPLE_A},
            )
            .scale(0.5)
            .move_to(circle0.get_center())
        )
        curve0 = CubicBezier(
            center_circle.get_edge_center(RIGHT),
            center_circle.get_center() + DR,
            circle0.get_center() + LEFT + UP,
            circle0.get_edge_center(LEFT),
        )

        self.play(ShowCreation(center_circle), Write(center_text))
        self.wait()
        self.play(ShowCreation(curve0))
        self.wait()
        self.play(Write(text0), ShowCreation(circle0))
        self.wait()

        circle1 = (
            Rectangle().scale(0.5).next_to(center_circle, direction=DOWN, buff=1.2)
        )
        text1 = (
            Text("建立健康边界", t2c={"健康": GREEN_D}).scale(0.5).move_to(circle1.get_center())
        )
        curve1 = CubicBezier(
            center_circle.get_edge_center(DOWN),
            center_circle.get_edge_center(DOWN) + 0.5 * DR,
            circle1.get_edge_center(UP) + 0.5 * UL,
            circle1.get_edge_center(UP),
        )

        self.play(ShowCreation(curve1))
        self.wait()
        self.play(ShowCreation(circle1), Write(text1))
        self.wait()

        circle2 = Rectangle().scale(0.5).next_to(center_circle, direction=UP, buff=1.5)
        text2 = (
            Text("CPTSD", t2c={"C": ORANGE}).scale(0.5).move_to(circle2.get_center())
        )
        text2_additon = (
            Text("复杂(Complex)创伤后应激障碍", t2c={"复杂(Complex)": ORANGE})
            .scale(0.8)
            .next_to(text2, RIGHT, buff=1)
        )

        curve2 = CubicBezier(
            center_circle.get_edge_center(UP),
            center_circle.get_center() + UL,
            circle2.get_center() + DR,
            circle2.get_edge_center(DOWN),
        )

        self.play(ShowCreation(curve2))
        self.wait()
        self.play(ShowCreation(circle2), Write(text2))
        self.wait()
        self.play(Write(text2_additon))
        self.wait()

        circle3 = Rectangle().scale(0.4).next_to(center_circle, direction=LEFT, buff=1)
        text3 = (
            Text("寻求支持", t2c={"支持": TEAL_B}).scale(0.5).move_to(circle3.get_center())
        )

        curve3 = CubicBezier(
            center_circle.get_edge_center(LEFT),
            center_circle.get_edge_center(LEFT) + 0.4 * UL,
            circle3.get_edge_center(RIGHT) + 0.4 * DR,
            circle3.get_edge_center(RIGHT),
        )

        self.play(ShowCreation(curve3))
        self.wait()
        self.play(ShowCreation(circle3), Write(text3))
        self.wait()

        detail_texts = ["寻求医生或心理咨询", "找信任的人倾诉", "学习与自我疗愈"]

        lines_with_texts = VGroup()
        starting_point = circle3.get_edge_center(LEFT)

        directions = [UP + LEFT, LEFT, DOWN + LEFT]

        for i, text in enumerate(detail_texts):
            elbow = Elbow(angle=0)
            elbow.set_points_as_corners(
                [starting_point, starting_point + directions[i]]
            )

            text_mob = Text(text, font_size=24).next_to(
                elbow.get_end(), directions[i], buff=0.15
            )

            line_with_text = VGroup(elbow, text_mob)
            lines_with_texts.add(line_with_text)

        for line_with_text in lines_with_texts:
            self.play(ShowCreation(line_with_text[0]))
            self.play(Write(line_with_text[1]))
            self.wait()

        self.play(
            FadeOut(
                VGroup(
                    center_circle,
                    center_text,
                    circle0,
                    text0,
                    circle1,
                    text1,
                    circle2,
                    text2,
                    text2_additon,
                    circle3,
                    text3,
                    lines_with_texts,
                    curve0,
                    curve1,
                    curve2,
                    curve3,
                )
            )
        )


class End(Scene):
    def construct(self):
        xt1 = (
            SVGMobject(svg_path + "xtv5.svg")
            .scale(3.2)
            .set_fill(BLACK, 1)
            .set_stroke(WHITE, 2.5, 1)
        )
        self.play(ShowCreation(xt1), run_time=3)
        self.wait()
        xt1.generate_target()
        xt1.target.scale(0.6).to_edge(DR).shift(LEFT * 0.4 + DOWN * 0.1)
        self.play(MoveToTarget(xt1), run_time=2)
        bubble = Bubble(height=4, width=6.5, direction=RIGHT)
        text = (
            Text(
                """
            生命挥洒的乐章，是经历与重生的交响
            结束不是终点，而是新生的起始
            """,
                t2c={"新生": GREEN},
            )
            .scale(0.65)
            .shift(LEFT * 0.15)
        )
        self.play(ShowCreation(bubble), Write(text))
        self.wait(2)

        self.play(FadeOut(VGroup(xt1, bubble, text)))


class AxesLabel(VGroup):
    def __init__(self, axes, x, label, buff=0.3, **kwargs):
        label = Text(label).scale(0.7).next_to(axes.coords_to_point(x, 0), DOWN * 1.2)
        VGroup.__init__(self, label, **kwargs)


class Cover(Scene):
    def construct(self) -> None:
        title = (
            Text("自恋型虐待", color=YELLOW)
            .scale(2.8)
            .to_edge(UL, buff=0.8)
            .shift(RIGHT * 0.2)
        )

        # 右上角斜着的NPD
        npd = (
            Text("NPD", color=RED)
            .scale(3)
            .to_edge(UR, buff=0.8)
            .shift(DOWN + LEFT * 1.4)
            .rotate(-PI / 5)
        )

        # 招数与应对
        trick = (
            Text(
                """
                     招数
                      与
                     应对
                     """,
                color=BLUE,
            )
            .scale(1.8)
            .to_edge(DR, buff=0.8)
            .shift(LEFT*1.6)
        )
        self.add(title)
        self.add(npd)
        self.add(trick)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = f"manimgl {module_name} Respond -s -ow"
    os.system(command)
