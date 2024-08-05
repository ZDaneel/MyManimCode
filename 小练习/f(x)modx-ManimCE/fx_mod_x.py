from manim import *

class CombinedScene(Scene):
    CONFIG = {
        "number_of_lines": 100,
        "gradient_colors": [PINK, DARK_BLUE, RED],
        "end_value": 0.3,
        "total_time": 20,
        "func": lambda t: 10 * t,
    }

    def setup(self):
        for key, value in self.CONFIG.items():
            setattr(self, key, value)

    def construct(self):
        self.play_mod_n_animation()

    def play_mod_n_animation(self):
        circle = Circle(radius=(config.frame_height - 1) / 2)
        circle.to_edge(RIGHT, buff=1)
        self.play(Create(circle))

        func_x_label = MathTex("f(x)=x").scale(2).to_edge(UL).shift(RIGHT * 0.4)
        self.play(Write(func_x_label))

        # Show figures for f(x)=x
        for x, y in [(2, 10), (3, 60), (4, 100)]:
            self.display_figure(circle, x, y)

        func_tanh_label = MathTex("f(x)=\\tanh(x)").scale(1.8).to_edge(UL).shift(RIGHT * 0.4)
        self.play(Transform(func_x_label, func_tanh_label))

        # Show figures for f(x)=tanh(x)
        for x, y in [(2, 10), (3, 60), (4, 100)]:
            self.display_figure(circle, x, y, lambda x: np.tanh(x))

        func_10x_label = MathTex(r"f(x) = 10 \cdot x").scale(1.8).to_edge(UL).shift(RIGHT * 0.4)
        self.play(Transform(func_x_label, func_10x_label))

        label = MathTex("f(t,100)").scale(1.7).to_edge(LEFT, buff=2)
        self.play(Write(label))

        mod_tracker = ValueTracker(0)
        num_lines_tracker = ValueTracker(self.number_of_lines)
        func = self.func

        lines = self.create_mod_n_objects(
            circle, mod_tracker.get_value(), num_lines_tracker.get_value(), func=func
        )
        lines.add_updater(
            lambda mob: mob.become(
                self.create_mod_n_objects(
                    circle,
                    mod_tracker.get_value(),
                    num_lines_tracker.get_value(),
                    func=func,
                )
            )
        )
        lines.suspend_updating()
        self.add(circle, lines)
        self.wait(3)
        lines.resume_updating()
        self.add(circle, lines)
        self.play(
            mod_tracker.animate.set_value(self.end_value),
            rate_func=linear,
            run_time=self.total_time,
        )
        lines.clear_updaters()
        self.wait(3)
        self.play(FadeOut(lines))

        func_tan_label = MathTex("f(x)=10*\\tan(x)").scale(1.8).to_edge(UL).shift(RIGHT * 0.3)
        label2 = MathTex("f(t,256)").scale(1.7).to_edge(LEFT, buff=2)
        self.play(Transform(func_x_label, func_tan_label), Transform(label, label2))

        mod_tracker2 = ValueTracker(0)
        num_lines_tracker2 = ValueTracker(256)
        func2 = lambda t: 10 * np.tan(t)

        lines2 = self.create_mod_n_objects(
            circle, mod_tracker2.get_value(), num_lines_tracker2.get_value(), func=func2
        )
        lines2.add_updater(
            lambda mob: mob.become(
                self.create_mod_n_objects(
                    circle,
                    mod_tracker2.get_value(),
                    num_lines_tracker2.get_value(),
                    func=func2,
                )
            )
        )
        lines2.suspend_updating()
        self.add(circle, lines2)
        self.wait(3)
        lines2.resume_updating()
        self.add(circle, lines2)
        self.play(
            mod_tracker2.animate.set_value(self.end_value),
            rate_func=linear,
            run_time=self.total_time,
        )
        label3 = MathTex("f(t,512)").scale(1.8).to_edge(LEFT, buff=2)
        self.play(Transform(label, label3))
        self.play(
            num_lines_tracker2.animate.set_value(512), rate_func=linear, run_time=10
        )
        lines2.clear_updaters()
        self.wait(3)
        self.play(FadeOut(lines2))

    def display_figure(self, circle, x, y, func=lambda x: x):
        lines = self.create_mod_n_objects(circle, x, y, func)
        lines.set_stroke(width=1)
        label = MathTex(f"f({x},{y})").scale(1.7).to_edge(LEFT, buff=2)
        VGroup(circle, lines).to_edge(RIGHT, buff=1)
        self.play(Write(label), LaggedStartMap(Create, lines))
        self.wait(0.2)
        lines_c = lines.copy()
        lines_c.set_color(PINK)
        lines_c.set_stroke(width=3)
        self.play(LaggedStartMap(ShowPassingFlash, lines_c, time_width=0.4), run_time=2)
        self.wait(0.2)
        self.play(FadeOut(lines), Unwrite(label))

    def create_mod_n_objects(self, circle, x, y=None, func=lambda x: x):
        if y is None:
            y = self.number_of_lines
        lines = VGroup()
        for i in range(int(y)):
            start_proportion = (i % y) / y
            end_proportion = ((func(i * x)) % y) / y

            if i % 2 == 0:
                start_point = circle.point_from_proportion(start_proportion)
                end_point = circle.point_from_proportion(end_proportion)
            else:
                start_point = circle.point_from_proportion(end_proportion)
                end_point = circle.point_from_proportion(start_proportion)

            line = Line(start_point, end_point).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*self.gradient_colors)
        return lines


if __name__ == "__main__":
    from manim import config

    config.background_color = BLACK
    config.pixel_height = 720
    config.pixel_width = 1280
    config.frame_height = 7.0
    config.frame_width = 14.0
    scene = CombinedScene()
    scene.render()