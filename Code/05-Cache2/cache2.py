from manimlib import *

svg_path = "./images/svg/"


class AddressSequence(VGroup):
    def __init__(self, *addresses, **kwargs) -> None:
        super().__init__(**kwargs)
        self.addresses = [int(addr) for addr in addresses]

        self.address_mobs = VGroup()
        self.binary_mobs = VGroup()

        for addr in addresses:
            addr_mob = Text(str(addr))
            binary_mob = Text(format(addr, "04b"))  # 转换为4位二进制

            self.address_mobs.add(addr_mob)
            self.binary_mobs.add(binary_mob)

        self.address_mobs.arrange(DOWN, aligned_edge=ORIGIN)

        self.binary_mobs.arrange(DOWN, aligned_edge=LEFT)
        self.binary_mobs.next_to(self.address_mobs, RIGHT, buff=0.6)

        distance = self.address_mobs[0].get_top() - self.address_mobs[-1].get_bottom()
        self.arrow = Arrow(
            self.address_mobs[0].get_top() + UP * 0.8,
            self.address_mobs[0].get_top() + DOWN * distance + DOWN * 0.3,
        )
        self.arrow.next_to(self.address_mobs, LEFT, buff=0.4)
        self.add(self.address_mobs, self.binary_mobs, self.arrow)

    def get_address_row(self, address: int) -> VGroup:
        return VGroup(self.address_mobs[address], self.binary_mobs[address])

    def get_all_address_rows(self) -> VGroup:
        return VGroup(*[self.get_address_row(i) for i in range(len(self.addresses))])

    def get_binary_row(self, address: int) -> VGroup:
        return self.binary_mobs[address]

    def get_arrow(self) -> Arrow:
        return self.arrow

    def set_row_opacity(self, address: int, opacity: float) -> None:
        return self.get_address_row(address).animate.set_opacity(opacity)


class MemoryModel(VGroup):
    def __init__(
        self, rows=8, cell_width=1, cell_height=0.8, scale_factor=0.8, **kwargs
    ):
        super().__init__(**kwargs)
        self.create_memory_rows(rows, cell_width, cell_height)
        self.index_title = Text("块序号", color=RED_D).scale(0.6)
        self.index_title.next_to(self.row_groups[0][0], UP, buff=0.37)
        self.data_title = Text("内存数据", color=ORANGE).scale(0.6)
        self.data_title.next_to(self.row_groups[0][1], UP, buff=0.15).shift(RIGHT * 0.5)
        self.add(self.index_title, self.data_title)
        self.scale(scale_factor)

    def create_memory_rows(self, rows, cell_width, cell_height):
        self.row_groups = VGroup()
        for i in range(rows):
            rect_left = Rectangle(height=cell_height, width=cell_width)
            rect_right = Rectangle(height=cell_height, width=cell_width)
            rect_right.next_to(rect_left, RIGHT, buff=0)

            text_left = Text(f"D{i*2+1}", font_size=24, color=YELLOW).next_to(
                rect_left, ORIGIN
            )
            text_right = Text(f"D{i*2+2}", font_size=24, color=YELLOW).next_to(
                rect_right, ORIGIN
            )

            label = Text(str(i), color=BLUE).scale(1)
            label.next_to(rect_left, LEFT, buff=0.5)

            if 1 == i:
                label.shift(LEFT * 0.06)  # 修正位置

            row_group = VGroup(label, rect_left, text_left, rect_right, text_right)
            self.row_groups.add(row_group)
        self.row_groups.arrange(DOWN, aligned_edge=RIGHT, buff=0)
        self.add(self.row_groups)

    def get_memory_row(self, row: int) -> VGroup:
        return self.row_groups[row]


class CacheRow(VGroup):
    def __init__(
        self,
        row_index,
        cell_width,
        cell_height,
        show_label=True,
        show_lru=False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.row_index = row_index
        self.cell_width = cell_width
        self.cell_height = cell_height

        if show_lru:
            self.create_row_lru()
        else:
            self.create_row(show_label)

    def create_row(self, show_label):
        self.rect_valid = Rectangle(
            height=self.cell_height, width=self.cell_width * 0.4
        )
        self.rect_tag = Rectangle(height=self.cell_height, width=self.cell_width * 0.6)
        self.rect_left = Rectangle(height=self.cell_height, width=self.cell_width)
        self.rect_right = Rectangle(height=self.cell_height, width=self.cell_width)

        self.rect_tag.next_to(self.rect_valid, RIGHT, buff=0)
        self.rect_left.next_to(self.rect_tag, RIGHT, buff=0)
        self.rect_right.next_to(self.rect_left, RIGHT, buff=0)

        self.text_valid = Text("0", font_size=30, color=TEAL_B).move_to(
            self.rect_valid.get_center()
        )
        self.text_tag = Text("", font_size=24, color=PURPLE_B).move_to(
            self.rect_tag.get_center()
        )
        self.text_left = Text("", font_size=24, color=YELLOW).move_to(
            self.rect_left.get_center()
        )
        self.text_right = Text("", font_size=24, color=YELLOW).move_to(
            self.rect_right.get_center()
        )

        if show_label:
            self.label = Text(str(self.row_index), color=BLUE).scale(1)
            self.label.next_to(self.rect_valid, LEFT, buff=0.5)

            if 1 == self.row_index:
                self.label.shift(LEFT * 0.06)  # 修正位置

        self.add(
            self.rect_valid,
            self.rect_tag,
            self.rect_left,
            self.rect_right,
            self.text_valid,
            self.text_tag,
            self.text_left,
            self.text_right,
        )

        if show_label:
            self.add(self.label)

    def create_row_lru(self):
        self.rect_lru = Rectangle(height=self.cell_height, width=self.cell_width * 0.5)
        self.rect_valid = Rectangle(
            height=self.cell_height, width=self.cell_width * 0.5
        )
        self.rect_tag = Rectangle(height=self.cell_height, width=self.cell_width * 0.6)
        self.rect_left = Rectangle(height=self.cell_height, width=self.cell_width)
        self.rect_right = Rectangle(height=self.cell_height, width=self.cell_width)

        self.rect_valid.next_to(self.rect_lru, RIGHT, buff=0)
        self.rect_tag.next_to(self.rect_valid, RIGHT, buff=0)
        self.rect_left.next_to(self.rect_tag, RIGHT, buff=0)
        self.rect_right.next_to(self.rect_left, RIGHT, buff=0)

        self.text_lru = Text("0", font_size=30, color=MAROON_B).move_to(
            self.rect_lru.get_center()
        )
        self.text_valid = Text("0", font_size=30, color=TEAL_B).move_to(
            self.rect_valid.get_center()
        )
        self.text_tag = Text("", font_size=24, color=PURPLE_B).move_to(
            self.rect_tag.get_center()
        )
        self.text_left = Text("", font_size=24, color=YELLOW).move_to(
            self.rect_left.get_center()
        )
        self.text_right = Text("", font_size=24, color=YELLOW).move_to(
            self.rect_right.get_center()
        )

        self.add(
            self.rect_lru,
            self.rect_valid,
            self.rect_tag,
            self.rect_left,
            self.rect_right,
            self.text_lru,
            self.text_valid,
            self.text_tag,
            self.text_left,
            self.text_right,
        )


class CacheModel(VGroup):
    def __init__(
        self,
        rows=4,
        cell_width=1,
        cell_height=0.8,
        scale_factor=0.8,
        show_label=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.create_cache_rows(rows, cell_width, cell_height, show_label)
        self.valid_title = Text("V", color=TEAL_B).scale(0.6)
        self.valid_title.next_to(self.row_groups[0].rect_valid, UP, buff=0.2).shift(
            LEFT * 0.02
        )
        self.tag_title = Text("标记", color=PURPLE_B).scale(0.6)
        self.tag_title.next_to(self.row_groups[0].rect_tag, UP, buff=0.15)
        self.data_title = Text("缓存数据", color=ORANGE).scale(0.6)
        self.data_title.next_to(self.row_groups[0].rect_left, UP, buff=0.15).shift(
            RIGHT * 0.5
        )
        self.add(self.valid_title, self.tag_title, self.data_title)
        self.scale(scale_factor)

    def create_cache_rows(self, rows, cell_width, cell_height, show_label):
        self.row_groups = VGroup()
        for i in range(rows):
            row = CacheRow(i, cell_width, cell_height, show_label)
            self.row_groups.add(row)

        self.row_groups.arrange(DOWN, aligned_edge=RIGHT, buff=0)
        self.add(self.row_groups)

    def get_cache_row(self, row: int) -> CacheRow:
        return self.row_groups[row]


class LruCacheModel(VGroup):
    def __init__(
        self,
        rows=4,
        cell_width=1,
        cell_height=0.8,
        scale_factor=0.8,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.create_cache_rows(rows, cell_width, cell_height)
        self.lru_title = Text("LRU", color=MAROON_B).scale(0.6)
        self.lru_title.next_to(self.row_groups[0].rect_lru, UP, buff=0.18)
        self.valid_title = Text("V", color=TEAL_B).scale(0.6)
        self.valid_title.next_to(self.row_groups[0].rect_valid, UP, buff=0.18).shift(
            LEFT * 0.02
        )
        self.tag_title = Text("标记", color=PURPLE_B).scale(0.6)
        self.tag_title.next_to(self.row_groups[0].rect_tag, UP, buff=0.15)
        self.data_title = Text("缓存数据", color=ORANGE).scale(0.6)
        self.data_title.next_to(self.row_groups[0].rect_left, UP, buff=0.15).shift(
            RIGHT * 0.5
        )
        self.add(self.lru_title, self.valid_title, self.tag_title, self.data_title)
        self.scale_factor = scale_factor
        self.scale(scale_factor)

    def create_cache_rows(self, rows, cell_width, cell_height):
        self.row_groups = VGroup()
        for i in range(rows):
            row = CacheRow(i, cell_width, cell_height, show_lru=True)
            self.row_groups.add(row)

        self.row_groups.arrange(DOWN, aligned_edge=RIGHT, buff=0)
        self.add(self.row_groups)

    def get_cache_row(self, row: int) -> CacheRow:
        return self.row_groups[row]

    def increase_lru(self, row_index: int, current_texts: list, set_index=-1):
        # set仅限于索引为2
        animations = []
        new_texts = []

        if set_index == -1:
            index_list = [0, 1, 2, 3]
        else:
            index_list = [0, 1]

        for i in index_list:
            if i != row_index:
                new_value = int(current_texts[i].text) + 1
                if set_index != 1:
                    new_text = Text(
                        str(new_value), font_size=28, color=MAROON_B
                    ).move_to(self.row_groups[i].rect_lru.get_center())
                else:
                    new_text = Text(
                        str(new_value), font_size=28, color=MAROON_B
                    ).move_to(self.row_groups[i + 2].rect_lru.get_center())
                anim = ReplacementTransform(current_texts[i], new_text)
                animations.append(anim)
                new_texts.append(new_text)
            else:
                if set_index != 1:
                    zero_text = Text("0", font_size=28, color=MAROON_B).move_to(
                        self.row_groups[i].rect_lru.get_center()
                    )
                else:
                    zero_text = Text("0", font_size=28, color=MAROON_B).move_to(
                        self.row_groups[i + 2].rect_lru.get_center()
                    )
                anim = ReplacementTransform(current_texts[i], zero_text)
                animations.append(anim)
                new_texts.append(zero_text)

        return new_texts, animations

    def create_set_rect_and_label(self):
        cache_colors = [BLUE_B, PINK]
        cache_labels = ["0", "1"]
        self.set_rects = VGroup()
        self.set_rect_labels = VGroup()
        for index, color in enumerate(cache_colors):
            cache_group_rect = Rectangle(
                height=2 * self.row_groups[0].get_height(),
                width=2.88 * self.scale_factor / 0.8,
                fill_opacity=0,
                stroke_color=color,
                stroke_width=4.5,
            )
            cache_group_rect.move_to(
                self.row_groups[2 * 1 * index].get_center()
                + DOWN * (3 * self.row_groups[0].get_height() / 6)
                + RIGHT * 0
            )
            cache_group_rect_label = (
                Text(cache_labels[index], color=color)
                .scale(0.8)
                .next_to(cache_group_rect, LEFT, buff=0.4)
            )
            self.set_rects.add(cache_group_rect)
            self.set_rect_labels.add(cache_group_rect_label)
        self.set_rects[0].shift(UP * 0.015)
        self.set_rects[1].shift(DOWN * 0.015)
        set_tilte = Text("组号", color=GREEN_B).scale(0.58)
        set_tilte.next_to(self.set_rect_labels, UP, buff=0.82)
        set_group = VGroup(self.set_rects, self.set_rect_labels, set_tilte)
        self.add(self.set_rects, self.set_rect_labels)
        return set_group


class TreeModel(VGroup):
    def __init__(
        self,
        cache_model,
        scale_factor=0.8,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.cache_model = cache_model
        self.create_tree()
        self.scale(scale_factor)

    def create_tree(self):
        self.tree = VGroup()
        # 节点
        self.root_node_rect = RoundedRectangle(
            height=0.6, width=0.8, corner_radius=0.2
        ).scale(0.8)
        self.root_node_rect.next_to(self.cache_model, LEFT, buff=2).shift(DOWN * 0.2)
        self.root_node_label = Text("", color=GOLD_C).scale(0.8)
        self.root_node_label.move_to(self.root_node_rect.get_center())
        self.tree.add(self.root_node_rect, self.root_node_label)
        self.up_node_rect = RoundedRectangle(
            height=0.6, width=0.8, corner_radius=0.2
        ).scale(0.8)
        self.up_node_rect.next_to(self.root_node_rect, UP, buff=0.22).shift(RIGHT * 1.2)
        self.up_node_label = Text("", color=GOLD_C).scale(0.8)
        self.up_node_label.move_to(self.up_node_rect.get_center())
        self.tree.add(self.up_node_rect, self.up_node_label)
        self.down_node_rect = RoundedRectangle(
            height=0.6, width=0.8, corner_radius=0.2
        ).scale(0.8)
        self.down_node_rect.next_to(self.root_node_rect, DOWN, buff=0.2).shift(
            RIGHT * 1.2
        )
        self.down_node_label = Text("", color=GOLD_C).scale(0.8)
        self.down_node_label.move_to(self.down_node_rect.get_center())
        self.tree.add(self.down_node_rect, self.down_node_label)
        # 箭头
        self.root_arrow_up = Arrow(
            self.root_node_rect.get_right() + LEFT * 0.05 + DOWN * 0.1,
            self.up_node_rect.get_left() + RIGHT * 0.05 + UP * 0.1,
            stroke_color=GREEN_C,
            stroke_width=3,
        ).set_opacity(0.4)
        self.root_arrow_down = Arrow(
            self.root_node_rect.get_right() + LEFT * 0.05 + UP * 0.1,
            self.down_node_rect.get_left() + RIGHT * 0.05 + DOWN * 0.1,
            stroke_color=GOLD_C,
            stroke_width=3,
        ).set_opacity(0.4)
        self.tree.add(self.root_arrow_up, self.root_arrow_down)
        self.up_arrow_up = Arrow(
            self.up_node_rect.get_right() + LEFT * 0.1 + DOWN * 0.05,
            self.cache_model.get_cache_row(0).get_left() + RIGHT * 0.1 + UP * 0.1,
            stroke_color=GREEN_C,
            stroke_width=3,
        ).set_opacity(0.4)
        self.up_arrow_down = Arrow(
            self.up_node_rect.get_right() + LEFT * 0.1 + UP * 0.05,
            self.cache_model.get_cache_row(1).get_left() + RIGHT * 0.1 + DOWN * 0.1,
            stroke_color=GOLD_C,
            stroke_width=3,
        ).set_opacity(0.4)
        self.tree.add(self.up_arrow_up, self.up_arrow_down)
        self.down_arrow_up = Arrow(
            self.down_node_rect.get_right() + LEFT * 0.1 + DOWN * 0.05,
            self.cache_model.get_cache_row(2).get_left() + RIGHT * 0.1 + UP * 0.1,
            stroke_color=GREEN_C,
            stroke_width=3,
        ).set_opacity(0.4)
        self.down_arrow_down = Arrow(
            self.down_node_rect.get_right() + LEFT * 0.1 + UP * 0.05,
            self.cache_model.get_cache_row(3).get_left() + RIGHT * 0.1 + DOWN * 0.1,
            stroke_color=GOLD_C,
            stroke_width=3,
        ).set_opacity(0.4)
        self.tree.add(self.down_arrow_up, self.down_arrow_down)
        self.add(self.tree)

    def create_arrow_opacity_animation(self, arrow: Arrow, opacity: float) -> Animation:
        return arrow.animate.set_opacity(opacity)

    def create_node_label_animation(self, current_label: Text, new_label_str: str):
        if 0 == int(new_label_str):
            label_color = GOLD
        else:
            label_color = GREEN
        new_label = Text(new_label_str, color=label_color).scale(0.8)
        new_label.move_to(current_label.get_center())
        return new_label, ReplacementTransform(current_label, new_label)


class BitTable(VGroup):
    def __init__(self, rect_size, rect_count=4, **kwargs):
        super().__init__(**kwargs)
        self.rects = VGroup(
            *[Rectangle(height=rect_size, width=rect_size) for _ in range(rect_count)]
        )
        self.rects.arrange(RIGHT, buff=0)
        self.add(self.rects)

    def fill_rects_with_text(self, fill_info):
        """
        fill_info: List of tuples [(index, length, color, text), ...]
        Example: [(0, 1, RED, "Text1"), (2, 2, BLUE, "Text2")]
        """
        for index, length, color, text in fill_info:
            if 0 <= index < len(self.rects):
                if 1 == length:
                    self.rects[index].set_fill(color, opacity=0.8)
                    text_mob = Text(text, color=color).scale(0.4)
                    text_mob.next_to(self.rects[index], UP, buff=0.1)
                    self.add(text_mob)
                else:
                    combination_group = VGroup()
                    for i in range(length):
                        self.rects[index + i].set_fill(color, opacity=0.8)
                        combination_group.add(self.rects[index + i])
                    text_mob = Text(text, color=color).scale(0.4)
                    text_mob.next_to(combination_group, UP, buff=0.1)
                    self.add(text_mob)

    def get_rect(self, index: int) -> Rectangle:
        return self.rects[index]


def create_seq2cache_bit_text_copy_and_animation(
    address_sequence: AddressSequence, cache_bit_table: BitTable, row_number: int
):
    text_copy_group = VGroup()
    animation_list = []
    for index in range(4):
        text = address_sequence.get_binary_row(row_number)[index]
        text_copy = text.copy()
        move_animation = text_copy.animate.move_to(
            cache_bit_table.get_rect(index).get_center()
        )
        text_copy_group.add(text_copy)
        animation_list.append(move_animation)
    return text_copy_group, animation_list


def create_seq2memory_bit_text_copy_and_animation(
    address_sequence: AddressSequence, memory_bit_table: BitTable, row_number: int
):
    text_copy_group = VGroup()
    animation_list = []
    for index in range(4):
        text = address_sequence.get_binary_row(row_number)[index]
        text_copy = text.copy()
        move_animation = text_copy.animate.move_to(
            memory_bit_table.get_rect(index).get_center()
        )
        text_copy_group.add(text_copy)
        animation_list.append(move_animation)
    return text_copy_group, animation_list


def create_memory2cache_text_copy_and_animation(
    memory_model: MemoryModel,
    cache_model: CacheModel,
    memory_row_number: int,
    cache_row_number: int,
    text_scale_factor=1.2,
):
    animation_list = []
    text_left = memory_model.get_memory_row(memory_row_number)[2]
    text_right = memory_model.get_memory_row(memory_row_number)[4]
    text_left_copy = text_left.copy().scale(text_scale_factor)
    text_right_copy = text_right.copy().scale(text_scale_factor)
    move_animation_left = text_left_copy.animate.move_to(
        cache_model.get_cache_row(cache_row_number).rect_left.get_center()
    )
    move_animation_right = text_right_copy.animate.move_to(
        cache_model.get_cache_row(cache_row_number).rect_right.get_center()
    )
    text_copy_group = VGroup(text_left_copy, text_right_copy)
    animation_list.append(move_animation_left)
    animation_list.append(move_animation_right)
    return text_copy_group, animation_list


def create_cache_tag_bits2table_text_and_animation(
    cache_model: CacheModel,
    cache_row_number: int,
    cache_tag_bits: VGroup,
    tag_text_str: str,
    text_scale_factor=0.6,
):
    tag_text = Text(tag_text_str, color=PURPLE_B).scale(text_scale_factor)
    tag_text.move_to(cache_model.get_cache_row(cache_row_number).rect_tag.get_center())

    move_animation = TransformFromCopy(cache_tag_bits, tag_text)

    return tag_text, move_animation


class Cache2Intro(Scene):
    def construct(self) -> None:
        new_title = Text("缓存(Cache)", color=MAROON_B).scale(1.4)
        new_title.to_edge(UP + LEFT)
        self.play(Write(new_title), run_time=1.5)
        self.wait()
        rect_height = 9 / 4
        rect_width = 16 / 4

        model_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        model_rect.move_to(ORIGIN)
        model_text = Text("1. 什么是缓存", color=BLUE).scale(0.8)
        model_text.next_to(model_rect.get_top(), UP, buff=0.1)
        model_group = VGroup(model_rect, model_text)

        byte_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        byte_rect.move_to(ORIGIN)
        byte_text = Text("2. 块的概念", color=BLUE).scale(0.8)
        byte_text.next_to(byte_rect.get_top(), UP, buff=0.1)
        byte_group = VGroup(byte_rect, byte_text)

        address_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        address_rect.move_to(ORIGIN)
        address_text = Text("3. 缓存映射", color=BLUE).scale(0.8)
        address_text.next_to(address_rect.get_top(), UP, buff=0.1)
        address_group = VGroup(address_rect, address_text)

        double_rect = Rectangle(
            height=rect_height, width=rect_width, stroke_width=1
        ).set_fill(BLACK, opacity=1)
        double_rect.move_to(ORIGIN)
        double_text = Text("4. 缓存结构", color=BLUE).scale(0.8)
        double_text.next_to(double_rect.get_top(), UP, buff=0.1)
        double_group = VGroup(double_rect, double_text)

        # 将四个矩形放置到合适的位置
        model_group.next_to(new_title, DOWN, buff=0.5).align_to(new_title, LEFT).shift(
            RIGHT * 1.8 + UP * 0.45
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
        self.play(
            FadeOut(
                VGroup(new_title, model_group, byte_group, address_group, double_group)
            )
        )
        self.wait()

        xt = (
            SVGMobject(svg_path + "qxt.svg")
            .scale(3.2)
            .set_fill(BLACK, 1)
            .set_stroke(WHITE, 2.5, 1)
        )
        xt.scale(0.65).to_edge(DR).shift(LEFT * 0.4 + DOWN * 0.1)
        qxx = (
            SVGMobject(svg_path + "qxx.svg")
            .scale(1)
            .set_fill(BLACK, 1)
            .set_stroke(WHITE, 2.5, 1)
        ).to_edge(DL)
        qxx_1 = qxx.copy().next_to(qxx, RIGHT, buff=0.1)
        qxx_2 = qxx.copy().next_to(qxx_1, RIGHT, buff=0.2)
        self.play(ShowCreation(xt))
        self.wait()
        self.play(ShowCreation(qxx), ShowCreation(qxx_1), ShowCreation(qxx_2))
        self.wait()
        intro_rect = (
            Rectangle(height=9 / 2, width=16 / 2)
            .set_fill(BLACK, opacity=1)
            .to_edge(UL)
            .shift(DOWN * 0.42 + RIGHT * 0.6)
        )
        title_1 = Text("缓存的运作机制", color=BLUE).scale(0.8).next_to(intro_rect, UP)
        self.play(ShowCreation(intro_rect), Write(title_1))
        self.wait()


class DirectMappingDisplay(Scene):
    def construct(self) -> None:
        direct_mapping_text = Text("直接映射").to_edge(UP + LEFT).scale(1.2)
        word_byte_text = (
            Text("1字(Word) = 4字节(Byte)", color=RED)
            .scale(0.7)
            .next_to(direct_mapping_text, DOWN, buff=0.4)
            .align_to(direct_mapping_text, LEFT)
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

        self.play(Write(direct_mapping_text))
        self.wait()
        self.play(Write(block_word_byte_group), run_time=2)
        self.wait()
        self.play(ShowCreation(block_word_byte_rect))
        self.wait()

        memory_model = MemoryModel()
        self.play(Write(memory_model), run_time=3)
        self.wait()
        self.play(FlashAround(memory_model.get_memory_row(0)[1:-1]))
        self.wait()
        self.play(FlashAround(memory_model.get_memory_row(0)[1]))
        self.play(FlashAround(memory_model.get_memory_row(0)[3]))
        self.wait()

        memory_model.generate_target()
        memory_model.target.shift(RIGHT * 5.4 + DOWN * 0.8)
        self.play(MoveToTarget(memory_model), run_time=2)
        self.wait()

        memory_bit_table = BitTable(rect_size=0.6)
        memory_bit_table.fill_rects_with_text(
            [
                (0, 3, RED_D, "块索引"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        self.play(Write(memory_bit_table), run_time=2)
        self.wait()
        memory_bit_table.generate_target()
        memory_bit_table.target.next_to(memory_model, UP, buff=0.5).shift(LEFT * 1.6)
        self.play(MoveToTarget(memory_bit_table), run_time=2)
        self.wait()

        cache_model = CacheModel(scale_factor=1)
        self.play(Write(cache_model), run_time=3)
        self.wait()
        cache_model.generate_target()
        cache_model.target.shift(DOWN * 0.8)
        self.play(MoveToTarget(cache_model), run_time=2)
        self.wait()

        cache_bit_table = BitTable(rect_size=0.6)
        cache_bit_table.fill_rects_with_text(
            [
                (0, 1, PURPLE_B, "标记"),
                (1, 2, GREEN_C, "索引"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        cache_bit_table.next_to(memory_bit_table, LEFT, buff=0.5).shift(LEFT * 1.6)
        self.play(Write(cache_bit_table), run_time=2)
        self.wait()

        direct_arrow_group = VGroup()
        direct_color_set = [RED_B, BLUE_B, GREEN_B, YELLOW_B]
        for i in range(8):
            j = i
            if i > 3:
                j = i - 4
            arrow = Arrow(
                memory_model.get_memory_row(i).get_left(),
                cache_model.get_cache_row(j).get_right(),
                buff=0.05,
                stroke_color=direct_color_set[j],
                stroke_width=2,
            )
            direct_arrow_group.add(arrow)

        self.play(ShowCreation(direct_arrow_group), run_time=2)
        self.wait()
        self.play(*[direct_arrow_group[i].animate.set_opacity(0.3) for i in range(8)])
        self.wait()

        sequence_text = Text("地址序列").scale(0.8)
        sequence_text.next_to(block_word_byte_rect, DOWN, buff=0.5)

        address_sequence = AddressSequence(0, 2, 3, 8)
        address_sequence.next_to(sequence_text, DOWN, buff=0.4)
        self.play(Write(sequence_text), run_time=2)
        self.wait()
        self.play(Write(address_sequence), run_time=3)
        self.wait()
        self.play(*[address_sequence.set_row_opacity(i, 0.5) for i in range(4)])
        self.wait()

        # 处理序列第一行
        self.play(address_sequence.set_row_opacity(0, 1))
        self.wait()
        (
            cache_bits_0,
            seq2cache_animations_0,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 0
        )
        self.play(*seq2cache_animations_0)
        self.wait()
        index_gruop_0 = VGroup(cache_bits_0[1], cache_bits_0[2])
        index_text_0 = Text("0", color=GREEN_C)
        index_text_0.next_to(index_gruop_0, DOWN, buff=0.3)
        self.play(TransformFromCopy(index_gruop_0, index_text_0))
        self.wait()
        index_arrow_0 = CurvedArrow(
            index_text_0.get_left(),
            cache_model.get_cache_row(0).get_left(),
            stroke_color=GREEN_C,
            stroke_width=3,
            angle=TAU / 3,
        )
        self.play(ShowCreation(index_arrow_0))
        self.play(FlashAround(cache_model.get_cache_row(0)))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_valid))
        self.wait()
        (
            memory_bits_0,
            seq2memory_animations_0,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 0
        )
        self.play(*seq2memory_animations_0)
        self.wait()
        memory_block_group_0 = VGroup(
            memory_bits_0[0], memory_bits_0[1], memory_bits_0[2]
        )
        memory_block_text_0 = Text("0", color=RED_D)
        memory_block_text_0.next_to(memory_block_group_0, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_0, memory_block_text_0))
        self.wait()
        block_arrow_0 = CurvedArrow(
            memory_block_text_0.get_bottom(),
            memory_model.get_memory_row(0).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_0))
        self.play(FlashAround(memory_model.get_memory_row(0)))
        self.play(FadeOut(block_arrow_0))
        self.wait()
        self.play(direct_arrow_group[0].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_0,
            memory2cache_animations_0,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 0, 0)
        self.play(*memory2cache_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_left.become(text_left_right_0[0])
        cache_model.get_cache_row(0).text_right.become(text_left_right_0[1])
        self.play(FadeOut(text_left_right_0))
        bits_tag_0 = VGroup(cache_bits_0[0])
        tag_text_0, tag_animations_0 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_0, "0"
        )
        self.play(tag_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_tag.become(tag_text_0)
        self.play(FadeOut(tag_text_0))
        valid_text_0 = Text("1", font_size=30, color=TEAL_B)
        valid_text_0.move_to(
            cache_model.get_cache_row(0).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(0).text_valid, valid_text_0))
        self.wait()
        offset_arrow_0 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(0).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_0))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_0,
                    index_text_0,
                    memory_bits_0,
                    memory_block_text_0,
                    bits_tag_0,
                    valid_text_0,
                    offset_arrow_0,
                    index_arrow_0,
                )
            )
        )
        self.wait()

        # 处理序列第二行
        self.play(address_sequence.set_row_opacity(0, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(1, 1))
        self.wait()
        (
            cache_bits_1,
            seq2cache_animations_1,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 1
        )
        self.play(*seq2cache_animations_1)
        self.wait()
        index_gruop_1 = VGroup(cache_bits_1[1], cache_bits_1[2])
        index_text_1 = Text("1", color=GREEN_C)
        index_text_1.next_to(index_gruop_1, DOWN, buff=0.3)
        self.play(TransformFromCopy(index_gruop_1, index_text_1))
        self.wait()
        index_arrow_1 = CurvedArrow(
            index_text_1.get_left(),
            cache_model.get_cache_row(1).get_left(),
            stroke_color=GREEN_C,
            stroke_width=3,
            angle=TAU / 3,
        )
        self.play(ShowCreation(index_arrow_1))
        self.play(FlashAround(cache_model.get_cache_row(1)))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_valid))
        self.wait()
        (
            memory_bits_1,
            seq2memory_animations_1,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 1
        )
        self.play(*seq2memory_animations_1)
        self.wait()
        memory_block_group_1 = VGroup(
            memory_bits_1[0], memory_bits_1[1], memory_bits_1[2]
        )
        memory_block_text_1 = Text("1", color=RED_D)
        memory_block_text_1.next_to(memory_block_group_1, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_1, memory_block_text_1))
        self.wait()
        block_arrow_1 = CurvedArrow(
            memory_block_text_1.get_bottom(),
            memory_model.get_memory_row(1).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_1))
        self.play(FlashAround(memory_model.get_memory_row(1)))
        self.play(FadeOut(block_arrow_1))
        self.wait()
        self.play(direct_arrow_group[1].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_1,
            memory2cache_animations_1,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 1, 1)
        self.play(*memory2cache_animations_1)
        self.wait()
        cache_model.get_cache_row(1).text_left.become(text_left_right_1[0])
        cache_model.get_cache_row(1).text_right.become(text_left_right_1[1])
        self.play(FadeOut(text_left_right_1))
        bits_tag_1 = VGroup(cache_bits_1[0])
        tag_text_1, tag_animations_1 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 1, bits_tag_1, "0"
        )
        self.play(tag_animations_1)
        self.wait()
        cache_model.get_cache_row(1).text_tag.become(tag_text_1)
        self.play(FadeOut(tag_text_1))
        valid_text_1 = Text("1", font_size=30, color=TEAL_B)
        valid_text_1.move_to(
            cache_model.get_cache_row(1).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(1).text_valid, valid_text_1))
        self.wait()
        offset_arrow_1 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(1).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_1))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_1,
                    index_text_1,
                    memory_bits_1,
                    memory_block_text_1,
                    bits_tag_1,
                    valid_text_1,
                    offset_arrow_1,
                    index_arrow_1,
                )
            )
        )

        # 处理序列第三行
        self.play(address_sequence.set_row_opacity(1, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(2, 1))
        self.wait()
        (
            cache_bits_2,
            seq2cache_animations_2,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 2
        )
        self.play(*seq2cache_animations_2)
        self.wait()
        index_gruop_2 = VGroup(cache_bits_2[1], cache_bits_2[2])
        index_text_2 = Text("1", color=GREEN_C)
        index_text_2.next_to(index_gruop_2, DOWN, buff=0.3)
        self.play(TransformFromCopy(index_gruop_2, index_text_2))
        self.wait()
        index_arrow_2 = CurvedArrow(
            index_text_2.get_left(),
            cache_model.get_cache_row(1).get_left(),
            stroke_color=GREEN_C,
            stroke_width=3,
            angle=TAU / 3,
        )
        self.play(ShowCreation(index_arrow_2))
        self.play(FlashAround(cache_model.get_cache_row(1)))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_valid))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_tag))
        self.wait()
        self.play(FlashAround(cache_bits_2[0]), run_time=2)
        self.wait()
        offset_arrow_2 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(1).text_right.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_2))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_right))
        self.wait()
        self.play(
            FadeOut(VGroup(cache_bits_2, index_text_2, offset_arrow_2, index_arrow_2))
        )
        self.wait()

        # 处理序列第四行
        self.play(address_sequence.set_row_opacity(2, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(3, 1))
        self.wait()
        (
            cache_bits_3,
            seq2cache_animations_3,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 3
        )
        self.play(*seq2cache_animations_3)
        self.wait()
        index_gruop_3 = VGroup(cache_bits_3[1], cache_bits_3[2])
        index_text_3 = Text("0", color=GREEN_C)
        index_text_3.next_to(index_gruop_3, DOWN, buff=0.3)
        self.play(TransformFromCopy(index_gruop_3, index_text_3))
        self.wait()
        index_arrow_3 = CurvedArrow(
            index_text_3.get_left(),
            cache_model.get_cache_row(0).get_left(),
            stroke_color=GREEN_C,
            stroke_width=3,
            angle=TAU / 3,
        )
        self.play(ShowCreation(index_arrow_3))
        self.play(FlashAround(cache_model.get_cache_row(0)))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_valid))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_tag))
        self.wait()
        self.play(FlashAround(cache_bits_3[0]), run_time=2)
        self.wait()
        (
            memory_bits_3,
            seq2memory_animations_3,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 3
        )
        self.play(*seq2memory_animations_3)
        self.wait()
        memory_block_group_3 = VGroup(
            memory_bits_3[0], memory_bits_3[1], memory_bits_3[2]
        )
        memory_block_text_3 = Text("4", color=RED_D)
        memory_block_text_3.next_to(memory_block_group_3, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_3, memory_block_text_3))
        self.wait()
        block_arrow_3 = CurvedArrow(
            memory_block_text_3.get_bottom(),
            memory_model.get_memory_row(4).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_3))
        self.play(FlashAround(memory_model.get_memory_row(4)))
        self.play(FadeOut(block_arrow_3))
        self.wait()

        self.play(direct_arrow_group[0].animate.set_opacity(0.4))
        self.wait()
        self.play(direct_arrow_group[4].animate.set_opacity(1))
        self.wait()
        # self.play(FadeOut(memory_block_text_3))
        # self.wait()
        # memory_block_group_4 = VGroup(
        #     memory_bits_3[0], memory_bits_3[1], memory_bits_3[2], memory_bits_3[3]
        # )
        # memory_block_text_4 = Text("8", color=TEAL_D).scale(0.9)
        # memory_block_text_4.next_to(memory_block_group_4, DOWN, buff=0.3)
        # self.play(TransformFromCopy(memory_block_group_4, memory_block_text_4))
        # self.wait()
        # module_text_1 = Text("%", color=TEAL_D).scale(0.9)
        # module_text_1.next_to(memory_block_text_4, RIGHT, buff=0.2)
        # module_text_2 = Text("4", color=TEAL_D).scale(0.9)
        # module_text_2.next_to(module_text_1, RIGHT, buff=0.2)
        # module_text_3 = Text("= 0", color=TEAL_D).scale(0.9)
        # module_text_3.next_to(module_text_2, RIGHT, buff=0.15)
        # self.play(Write(module_text_1))
        # self.wait()
        # self.play(Write(module_text_2))
        # self.wait()
        # self.play(Write(module_text_3))
        # self.wait()
        # self.play(FlashAround(cache_model.get_cache_row(0)), run_time=2)
        # self.wait()
        (
            text_left_right_3,
            memory2cache_animations_3,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 4, 0)
        self.play(
            FadeOut(
                VGroup(
                    cache_model.get_cache_row(0).text_left,
                    cache_model.get_cache_row(0).text_right,
                )
            )
        )
        self.wait()
        self.play(*memory2cache_animations_3)
        self.wait()
        bits_tag_3 = VGroup(cache_bits_3[0])
        tag_text_3, tag_animations_3 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_3, "1"
        )
        self.play(FadeOut(cache_model.get_cache_row(0).text_tag))
        self.wait()
        self.play(tag_animations_3)
        self.wait()
        offset_arrow_3 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(0).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_3))
        self.wait()
        self.play(Indicate(text_left_right_3[0]))
        self.wait()

        self.clear()


class FullMappingDisplay(Scene):
    def construct(self) -> None:
        direct_mapping_text = Text("全相联映射").to_edge(UP + LEFT).scale(1.2)
        word_byte_text = (
            Text("1字(Word) = 4字节(Byte)", color=RED)
            .scale(0.7)
            .next_to(direct_mapping_text, DOWN, buff=0.4)
            .align_to(direct_mapping_text, LEFT)
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

        self.play(Write(direct_mapping_text))
        self.wait()
        self.play(FadeIn(VGroup(block_word_byte_group, block_word_byte_rect)))
        self.wait()

        memory_model = MemoryModel().shift(RIGHT * 5.4 + DOWN * 0.8)
        memory_bit_table = BitTable(rect_size=0.6)
        memory_bit_table.fill_rects_with_text(
            [
                (0, 3, RED_D, "块索引"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        memory_bit_table.next_to(memory_model, UP, buff=0.5).shift(LEFT * 1.3)
        cache_model = CacheModel(scale_factor=1, show_label=False).shift(DOWN * 0.8)
        self.play(FadeIn(VGroup(memory_model, memory_bit_table, cache_model)))
        self.wait()
        cache_bit_table = BitTable(rect_size=0.6)
        cache_bit_table.fill_rects_with_text(
            [
                (0, 3, PURPLE_B, "标记"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        cache_bit_table.next_to(memory_bit_table, LEFT, buff=0.5).shift(LEFT * 1.4)
        self.play(Write(cache_bit_table), run_time=2)
        self.wait()

        fully_arrow_group = VGroup()
        fully_color_set = [RED_B, BLUE_B, GREEN_B, YELLOW_B]
        for i in range(4):
            for j in range(8):
                arrow = Arrow(
                    memory_model.get_memory_row(j).get_left(),
                    cache_model.get_cache_row(i).get_right(),
                    buff=0.05,
                    stroke_color=fully_color_set[i],
                    stroke_width=2,
                )
                fully_arrow_group.add(arrow)

        #self.play(ShowCreation(fully_arrow_group))
        # 32 0,8,16,24 1,9,17,25
        for i in range(8):
            self.play(
                ShowCreation(fully_arrow_group[i]), 
                ShowCreation(fully_arrow_group[8+i]),
                ShowCreation(fully_arrow_group[16+i]),
                ShowCreation(fully_arrow_group[24+i]),
                run_time=0.25
            )
        self.wait()
        self.play(*[fully_arrow_group[i].animate.set_opacity(0.3) for i in range(32)])
        self.wait()

        sequence_text = Text("地址序列").scale(0.8)
        sequence_text.next_to(block_word_byte_rect, DOWN, buff=0.5)

        address_sequence = AddressSequence(0, 2, 3, 8, 11, 13)
        address_sequence.next_to(sequence_text, DOWN, buff=0.4)
        self.play(Write(sequence_text), run_time=2)
        self.wait()
        self.play(Write(address_sequence), run_time=3)
        self.wait()
        self.play(*[address_sequence.set_row_opacity(i, 0.5) for i in range(6)])
        self.wait()

        # 处理序列第一行
        self.play(address_sequence.set_row_opacity(0, 1))
        self.wait()
        (
            cache_bits_0,
            seq2cache_animations_0,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 0
        )
        self.play(*seq2cache_animations_0)
        self.wait()
        tag_gruop_0 = VGroup(cache_bits_0[0], cache_bits_0[1], cache_bits_0[2])
        self.play(FlashAround(tag_gruop_0), run_time=2)
        self.wait()
        cache_model_tag_col = VGroup(
            cache_model.get_cache_row(0).rect_tag,
            cache_model.get_cache_row(1).rect_tag,
            cache_model.get_cache_row(2).rect_tag,
            cache_model.get_cache_row(3).rect_tag,
        )
        cache_model_valid_col = VGroup(
            cache_model.get_cache_row(0).text_valid,
            cache_model.get_cache_row(1).text_valid,
            cache_model.get_cache_row(2).text_valid,
            cache_model.get_cache_row(3).text_valid,
        )
        self.play(FlashAround(cache_model_tag_col), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_valid_col), run_time=2)
        self.wait()
        (
            memory_bits_0,
            seq2memory_animations_0,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 0
        )
        self.play(*seq2memory_animations_0)
        self.wait()
        memory_block_group_0 = VGroup(
            memory_bits_0[0], memory_bits_0[1], memory_bits_0[2]
        )
        memory_block_text_0 = Text("0", color=RED_D)
        memory_block_text_0.next_to(memory_block_group_0, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_0, memory_block_text_0))
        self.wait()
        block_arrow_0 = CurvedArrow(
            memory_block_text_0.get_bottom(),
            memory_model.get_memory_row(0).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_0))
        self.play(FlashAround(memory_model.get_memory_row(0)))
        self.play(FadeOut(block_arrow_0))
        self.wait()
        self.play(fully_arrow_group[0].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_0,
            memory2cache_animations_0,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 0, 0)
        self.play(*memory2cache_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_left.become(text_left_right_0[0])
        cache_model.get_cache_row(0).text_right.become(text_left_right_0[1])
        self.remove(text_left_right_0)
        bits_tag_0 = VGroup(cache_bits_0[0], cache_bits_0[1], cache_bits_0[2])
        tag_text_0, tag_animations_0 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_0, "000"
        )
        self.play(tag_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_tag.become(tag_text_0)
        self.remove(tag_text_0)
        valid_text_0 = Text("1", font_size=30, color=TEAL_B)
        valid_text_0.move_to(
            cache_model.get_cache_row(0).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(0).text_valid, valid_text_0))
        self.wait()
        offset_arrow_0 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(0).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_0))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_0,
                    memory_bits_0,
                    memory_block_text_0,
                    bits_tag_0,
                    valid_text_0,
                    offset_arrow_0,
                )
            )
        )
        self.wait()

        # 处理序列第二行
        self.play(address_sequence.set_row_opacity(0, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(1, 1))
        self.wait()
        (
            cache_bits_1,
            seq2cache_animations_1,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 1
        )
        self.play(*seq2cache_animations_1)
        self.wait()
        tag_gruop_1 = VGroup(cache_bits_1[0], cache_bits_1[1], cache_bits_1[2])
        self.play(FlashAround(tag_gruop_1), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_tag_col), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_valid_col), run_time=2)
        self.wait()
        (
            memory_bits_1,
            seq2memory_animations_1,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 1
        )
        self.play(*seq2memory_animations_1)
        self.wait()
        memory_block_group_1 = VGroup(
            memory_bits_1[0], memory_bits_1[1], memory_bits_1[2]
        )
        memory_block_text_1 = Text("1", color=RED_D)
        memory_block_text_1.next_to(memory_block_group_1, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_1, memory_block_text_1))
        self.wait()
        block_arrow_1 = CurvedArrow(
            memory_block_text_1.get_bottom(),
            memory_model.get_memory_row(1).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_1))
        self.play(FlashAround(memory_model.get_memory_row(1)))
        self.play(FadeOut(block_arrow_1))
        self.wait()
        self.play(fully_arrow_group[9].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_1,
            memory2cache_animations_1,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 1, 1)
        self.play(*memory2cache_animations_1)
        self.wait()
        cache_model.get_cache_row(1).text_left.become(text_left_right_1[0])
        cache_model.get_cache_row(1).text_right.become(text_left_right_1[1])
        self.remove(text_left_right_1)
        bits_tag_1 = VGroup(cache_bits_1[0], cache_bits_1[1], cache_bits_1[2])
        tag_text_1, tag_animations_1 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 1, bits_tag_1, "001"
        )
        self.play(tag_animations_1)
        self.wait()
        cache_model.get_cache_row(1).text_tag.become(tag_text_1)
        self.remove(tag_text_1)
        valid_text_1 = Text("1", font_size=30, color=TEAL_B)
        valid_text_1.move_to(
            cache_model.get_cache_row(1).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(1).text_valid, valid_text_1))
        self.wait()
        offset_arrow_1 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(1).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_1))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_1,
                    memory_bits_1,
                    memory_block_text_1,
                    bits_tag_1,
                    valid_text_1,
                    offset_arrow_1,
                )
            )
        )
        self.wait()

        # 处理序列第三行
        self.play(address_sequence.set_row_opacity(1, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(2, 1))
        self.wait()
        (
            cache_bits_2,
            seq2cache_animations_2,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 2
        )
        self.play(*seq2cache_animations_2)
        self.wait()
        tag_gruop_2 = VGroup(cache_bits_2[0], cache_bits_2[1], cache_bits_2[2])
        self.play(FlashAround(tag_gruop_2), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_tag_col), run_time=2)
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_tag))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_valid))
        self.wait()
        offset_arrow_2 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(1).text_right.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_2))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_right))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_2,
                    offset_arrow_2,
                )
            )
        )
        self.wait()

        # 处理序列第四行
        self.play(address_sequence.set_row_opacity(2, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(3, 1))
        self.wait()
        (
            cache_bits_3,
            seq2cache_animations_3,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 3
        )
        self.play(*seq2cache_animations_3)
        self.wait()
        tag_gruop_3 = VGroup(cache_bits_3[0], cache_bits_3[1], cache_bits_3[2])
        self.play(FlashAround(tag_gruop_3), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_tag_col), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_valid_col), run_time=2)
        self.wait()
        (
            memory_bits_3,
            seq2memory_animations_3,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 3
        )
        self.play(*seq2memory_animations_3)
        self.wait()
        memory_block_group_3 = VGroup(
            memory_bits_3[0], memory_bits_3[1], memory_bits_3[2]
        )
        memory_block_text_3 = Text("4", color=RED_D)
        memory_block_text_3.next_to(memory_block_group_3, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_3, memory_block_text_3))
        self.wait()
        block_arrow_3 = CurvedArrow(
            memory_block_text_3.get_bottom(),
            memory_model.get_memory_row(4).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_3))
        self.play(FlashAround(memory_model.get_memory_row(4)))
        self.play(FadeOut(block_arrow_3))
        self.wait()
        self.play(fully_arrow_group[20].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_3,
            memory2cache_animations_3,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 4, 2)
        self.play(*memory2cache_animations_3)
        self.wait()
        cache_model.get_cache_row(2).text_left.become(text_left_right_3[0])
        cache_model.get_cache_row(2).text_right.become(text_left_right_3[1])
        self.remove(text_left_right_3)
        bits_tag_3 = VGroup(cache_bits_3[0], cache_bits_3[1], cache_bits_3[2])
        tag_text_3, tag_animations_3 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 2, bits_tag_3, "100"
        )
        self.play(tag_animations_3)
        self.wait()
        cache_model.get_cache_row(2).text_tag.become(tag_text_3)
        self.remove(tag_text_3)
        valid_text_3 = Text("1", font_size=30, color=TEAL_B)
        valid_text_3.move_to(
            cache_model.get_cache_row(2).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(2).text_valid, valid_text_3))
        self.wait()
        offset_arrow_3 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(2).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_3))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(2).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_3,
                    memory_bits_3,
                    memory_block_text_3,
                    bits_tag_3,
                    valid_text_3,
                    offset_arrow_3,
                )
            )
        )
        self.wait()

        # 处理序列第五行
        self.play(address_sequence.set_row_opacity(3, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(4, 1))
        self.wait()
        (
            cache_bits_4,
            seq2cache_animations_4,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 4
        )
        self.play(*seq2cache_animations_4)
        self.wait()
        tag_gruop_4 = VGroup(cache_bits_4[0], cache_bits_4[1], cache_bits_4[2])
        self.play(FlashAround(tag_gruop_4), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_tag_col), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_valid_col), run_time=2)
        self.wait()
        (
            memory_bits_4,
            seq2memory_animations_4,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 4
        )
        self.play(*seq2memory_animations_4)
        self.wait()
        memory_block_group_4 = VGroup(
            memory_bits_4[0], memory_bits_4[1], memory_bits_4[2]
        )
        memory_block_text_4 = Text("5", color=RED_D)
        memory_block_text_4.next_to(memory_block_group_4, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_4, memory_block_text_4))
        self.wait()
        block_arrow_4 = CurvedArrow(
            memory_block_text_4.get_bottom(),
            memory_model.get_memory_row(5).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_4))
        self.play(FlashAround(memory_model.get_memory_row(5)))
        self.play(FadeOut(block_arrow_4))
        self.wait()
        self.play(fully_arrow_group[29].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_4,
            memory2cache_animations_4,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 5, 3)
        self.play(*memory2cache_animations_4)
        self.wait()
        cache_model.get_cache_row(3).text_left.become(text_left_right_4[0])
        cache_model.get_cache_row(3).text_right.become(text_left_right_4[1])
        self.remove(text_left_right_4)
        bits_tag_4 = VGroup(cache_bits_4[0], cache_bits_4[1], cache_bits_4[2])
        tag_text_4, tag_animations_4 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 3, bits_tag_4, "101"
        )
        self.play(tag_animations_4)
        self.wait()
        cache_model.get_cache_row(3).text_tag.become(tag_text_4)
        self.remove(tag_text_4)
        valid_text_4 = Text("1", font_size=30, color=TEAL_B)
        valid_text_4.move_to(
            cache_model.get_cache_row(3).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(3).text_valid, valid_text_4))
        self.wait()
        offset_arrow_4 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(3).text_right.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_4))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(3).text_right))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_4,
                    memory_bits_4,
                    memory_block_text_4,
                    bits_tag_4,
                    valid_text_4,
                    offset_arrow_4,
                )
            )
        )
        self.wait()

        # 处理序列第六行
        self.play(address_sequence.set_row_opacity(4, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(5, 1))
        self.wait()
        (
            cache_bits_5,
            seq2cache_animations_5,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 5
        )
        self.play(*seq2cache_animations_5)
        self.wait()
        tag_gruop_5 = VGroup(cache_bits_5[0], cache_bits_5[1], cache_bits_5[2])
        self.play(FlashAround(tag_gruop_5), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_tag_col), run_time=2)
        self.wait()
        self.play(FlashAround(cache_model_valid_col), run_time=2)
        self.wait()


class LruExplain(Scene):
    def construct(self) -> None:
        title = Text("缓存替换策略", color=WHITE).scale(1.5)

        cache_replace_img = (
            ImageMobject("cache_replace.png").scale(1.2).shift(DOWN * 0.4)
        )
        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP).scale(0.8))
        self.wait()
        line = Line(LEFT, RIGHT, color=WHITE).scale(6)
        line.next_to(title, DOWN, buff=0.3)
        self.play(ShowCreation(line))
        self.wait()
        self.play(FadeIn(cache_replace_img))
        self.wait()
        self.play(FadeOut(cache_replace_img))
        self.wait()

        # 首先出现LRU三个字母，然后L左移，R右移，出现小写字母Lease Recently Used
        l_text = Text("L", color=RED).scale(3)
        r_text = Text("R", color=YELLOW).scale(3)
        u_text = Text("U", color=BLUE).scale(3)
        l_text.next_to(line, DOWN, buff=0.3).shift(LEFT * 2 + DOWN)
        r_text.next_to(l_text, RIGHT, buff=0.3)
        u_text.next_to(r_text, RIGHT, buff=0.3)

        lru_group = VGroup(l_text, r_text, u_text)
        self.play(Write(lru_group))
        self.wait()
        animations = [
            l_text.animate.shift(LEFT * 1.6),
            u_text.animate.shift(RIGHT * 2.8),
        ]
        self.play(*animations)

        l_extra_text = Text("east", color=RED).scale(2)
        l_extra_text.next_to(l_text, RIGHT, buff=0.07).shift(DOWN * 0.2)
        r_extra_text = Text("ecently", color=YELLOW).scale(2)
        r_extra_text.next_to(r_text, RIGHT, buff=0.07).shift(DOWN * 0.2)
        u_extra_text = Text("sed", color=BLUE).scale(2)
        u_extra_text.next_to(u_text, RIGHT, buff=0.07).shift(DOWN * 0.17)

        self.play(Write(l_extra_text), Write(r_extra_text), Write(u_extra_text))
        self.wait()

        lru_group.add(l_extra_text, r_extra_text, u_extra_text)

        lru_ch_title = Text("最近最少使用", t2c={"最近": RED, "最少": YELLOW, "使用": BLUE}).scale(
            2
        )
        lru_ch_title.next_to(lru_group, DOWN, buff=0.3)
        self.play(Write(lru_ch_title))
        self.wait()

        lru_group.add(lru_ch_title)
        lru_group.generate_target()
        lru_group.target.scale(0.6).next_to(line, DOWN, buff=0.3).shift(LEFT * 3.3)
        self.play(MoveToTarget(lru_group))
        self.wait()

        lru_explain_text = Text("原则: 最近访问过的数据在不久的将来可能会被再次访问", color=WHITE).scale(0.8)
        lru_explain_text.next_to(lru_ch_title, DOWN, buff=0.3).shift(RIGHT * 2)
        self.play(Write(lru_explain_text))
        self.wait()

        counter_title = Text("计数器法", color=MAROON_B).scale(1)
        counter_title.next_to(lru_explain_text, DOWN, buff=0.5).shift(LEFT * 2.2)
        self.play(Write(counter_title))
        self.wait()
        counter_explain_text = Text(
            "每个缓存行有一个计数器\n" "表示自上次访问以来的时长\n" "替换计数器值最高的行",
            color=WHITE,
        ).scale(0.8)
        counter_explain_text.next_to(counter_title, DOWN, buff=0.4).shift(RIGHT * 0.4)
        self.play(Write(counter_explain_text))
        self.wait()
        divier_line1 = Line(UP * 0.5, DOWN * 0.5, color=WHITE).scale(3)
        divier_line1.next_to(counter_explain_text, RIGHT, buff=0.3).shift(RIGHT * 0.6)
        self.play(ShowCreation(divier_line1))
        self.wait()

        # 伪LRU
        tree_title = Text("树结构伪LRU法", color=GOLD).scale(1)
        tree_title.next_to(counter_title, RIGHT, buff=0.5).shift(RIGHT * 4)
        self.play(Write(tree_title))
        self.wait()
        tree_explain_text = Text(
            "使用二叉树跟踪访问模式\n" "树节点的状态决定替换策略\n" "虽是伪LRU, 但更高效",
            color=WHITE,
        ).scale(0.8)
        tree_explain_text.next_to(tree_title, DOWN, buff=0.4).shift(RIGHT * 0.2)
        self.play(Write(tree_explain_text))
        self.wait()


class FullMappingDisplayLru(Scene):
    def construct(self) -> None:
        basic_group = VGroup()
        direct_mapping_text = Text("全相联映射").to_edge(UP + LEFT).scale(1.2)
        word_byte_text = (
            Text("1字(Word) = 4字节(Byte)", color=RED)
            .scale(0.7)
            .next_to(direct_mapping_text, DOWN, buff=0.4)
            .align_to(direct_mapping_text, LEFT)
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
        basic_group.add(
            direct_mapping_text, block_word_byte_rect, block_word_byte_group
        )
        memory_model = MemoryModel().shift(RIGHT * 5.4 + DOWN * 0.8)
        memory_bit_table = BitTable(rect_size=0.6)
        memory_bit_table.fill_rects_with_text(
            [
                (0, 3, RED_D, "块索引"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        memory_bit_table.next_to(memory_model, UP, buff=0.5).shift(LEFT * 1.3)
        cache_model = CacheModel(scale_factor=1, show_label=False).shift(DOWN * 0.8)
        basic_group.add(memory_model, memory_bit_table, cache_model)
        cache_bit_table = BitTable(rect_size=0.6)
        cache_bit_table.fill_rects_with_text(
            [
                (0, 3, PURPLE_B, "标记"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        cache_bit_table.next_to(memory_bit_table, LEFT, buff=0.5).shift(LEFT * 1.4)
        fully_arrow_group = VGroup()
        fully_color_set = [RED_B, BLUE_B, GREEN_B, YELLOW_B]
        for i in range(4):
            for j in range(8):
                arrow = Arrow(
                    memory_model.get_memory_row(j).get_left(),
                    cache_model.get_cache_row(i).get_right(),
                    buff=0.05,
                    stroke_color=fully_color_set[i],
                    stroke_width=2,
                ).set_opacity(0.3)
                fully_arrow_group.add(arrow)
        basic_group.add(cache_bit_table, fully_arrow_group)
        sequence_text = Text("地址序列").scale(0.8)
        sequence_text.next_to(block_word_byte_rect, DOWN, buff=0.5)

        address_sequence = AddressSequence(0, 2, 3, 8, 11, 13)
        address_sequence.next_to(sequence_text, DOWN, buff=0.4)
        for i in range(6):
            address_sequence.get_address_row(i).set_opacity(0.3)
        basic_group.add(sequence_text, address_sequence)

        self.play(FadeIn(basic_group))
        self.wait()

        lru_cache_model = LruCacheModel(scale_factor=1)
        lru_cache_model.move_to(cache_model.get_center()).shift(LEFT * 0.3)
        self.play(ReplacementTransform(cache_model, lru_cache_model))
        self.wait()

        # 处理序列第一行
        self.play(address_sequence.set_row_opacity(0, 1))
        self.wait()
        (
            cache_bits_0,
            seq2cache_animations_0,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 0
        )
        self.play(*seq2cache_animations_0)
        self.wait()

        (
            memory_bits_0,
            seq2memory_animations_0,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 0
        )
        self.play(*seq2memory_animations_0)
        self.wait()

        memory_block_group_0 = VGroup(
            memory_bits_0[0], memory_bits_0[1], memory_bits_0[2]
        )
        memory_block_text_0 = Text("0", color=RED_D)
        memory_block_text_0.next_to(memory_block_group_0, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_0, memory_block_text_0))
        self.wait()

        self.play(fully_arrow_group[0].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_0,
            memory2cache_animations_0,
        ) = create_memory2cache_text_copy_and_animation(
            memory_model, lru_cache_model, 0, 0
        )
        self.play(*memory2cache_animations_0)
        self.wait()
        lru_cache_model.get_cache_row(0).text_left.become(text_left_right_0[0])
        lru_cache_model.get_cache_row(0).text_right.become(text_left_right_0[1])
        self.remove(text_left_right_0)
        bits_tag_0 = VGroup(cache_bits_0[0], cache_bits_0[1], cache_bits_0[2])
        tag_text_0, tag_animations_0 = create_cache_tag_bits2table_text_and_animation(
            lru_cache_model, 0, bits_tag_0, "000"
        )
        self.play(tag_animations_0)
        self.wait()
        lru_cache_model.get_cache_row(0).text_tag.become(tag_text_0)
        self.remove(tag_text_0)
        valid_text_0 = Text("1", font_size=30, color=TEAL_B)
        valid_text_0.move_to(
            lru_cache_model.get_cache_row(0).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(lru_cache_model.get_cache_row(0).text_valid, valid_text_0))
        self.wait()

        self.play(Indicate(lru_cache_model.get_cache_row(0).text_lru))
        self.wait()

        init_lru_list = []
        for i in range(4):
            init_lru_list.append(lru_cache_model.get_cache_row(i).text_lru)
        lru_texts_0, lru_animations_0 = lru_cache_model.increase_lru(0, init_lru_list)
        self.play(*lru_animations_0)
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_0,
                    memory_bits_0,
                    memory_block_text_0,
                    bits_tag_0,
                    valid_text_0,
                )
            )
        )
        self.wait()

        # 处理序列第二行
        self.play(address_sequence.set_row_opacity(0, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(1, 1))
        self.wait()
        (
            cache_bits_1,
            seq2cache_animations_1,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 1
        )
        self.play(*seq2cache_animations_1)
        self.wait()
        (
            memory_bits_1,
            seq2memory_animations_1,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 1
        )
        self.play(*seq2memory_animations_1)
        self.wait()
        memory_block_group_1 = VGroup(
            memory_bits_1[0], memory_bits_1[1], memory_bits_1[2]
        )
        memory_block_text_1 = Text("1", color=RED_D)
        memory_block_text_1.next_to(memory_block_group_1, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_1, memory_block_text_1))
        self.wait()
        self.play(fully_arrow_group[9].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_1,
            memory2cache_animations_1,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 1, 1)
        self.play(*memory2cache_animations_1)
        self.wait()
        lru_cache_model.get_cache_row(1).text_left.become(text_left_right_1[0])
        lru_cache_model.get_cache_row(1).text_right.become(text_left_right_1[1])
        self.remove(text_left_right_1)
        bits_tag_1 = VGroup(cache_bits_1[0], cache_bits_1[1], cache_bits_1[2])
        tag_text_1, tag_animations_1 = create_cache_tag_bits2table_text_and_animation(
            lru_cache_model, 1, bits_tag_1, "001"
        )
        self.play(tag_animations_1)
        self.wait()
        lru_cache_model.get_cache_row(1).text_tag.become(tag_text_1)
        self.remove(tag_text_1)
        valid_text_1 = Text("1", font_size=30, color=TEAL_B)
        valid_text_1.move_to(
            lru_cache_model.get_cache_row(1).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(lru_cache_model.get_cache_row(1).text_valid, valid_text_1))
        self.wait()
        lru_texts_1, lru_animations_1 = lru_cache_model.increase_lru(1, lru_texts_0)
        self.play(*lru_animations_1)
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_1,
                    memory_bits_1,
                    memory_block_text_1,
                    bits_tag_1,
                    valid_text_1,
                )
            )
        )
        self.wait()

        # 处理序列第三行
        self.play(address_sequence.set_row_opacity(1, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(2, 1))
        self.wait()
        (
            cache_bits_2,
            seq2cache_animations_2,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 2
        )
        self.play(*seq2cache_animations_2)
        self.wait()
        self.play(Indicate(lru_texts_1[1]))
        self.wait()
        lru_texts_2, lru_animations_2 = lru_cache_model.increase_lru(1, lru_texts_1)
        self.play(*lru_animations_2)
        self.wait()
        self.play(FadeOut(VGroup(cache_bits_2)))
        self.wait()

        # 处理序列第四行
        self.play(address_sequence.set_row_opacity(2, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(3, 1))
        self.wait()
        (
            cache_bits_3,
            seq2cache_animations_3,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 3
        )
        self.play(*seq2cache_animations_3)
        self.wait()
        (
            memory_bits_3,
            seq2memory_animations_3,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 3
        )
        self.play(*seq2memory_animations_3)
        self.wait()
        memory_block_group_3 = VGroup(
            memory_bits_3[0], memory_bits_3[1], memory_bits_3[2]
        )
        memory_block_text_3 = Text("4", color=RED_D)
        memory_block_text_3.next_to(memory_block_group_3, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_3, memory_block_text_3))
        self.wait()
        self.play(fully_arrow_group[20].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_3,
            memory2cache_animations_3,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 4, 2)
        self.play(*memory2cache_animations_3)
        self.wait()
        lru_cache_model.get_cache_row(2).text_left.become(text_left_right_3[0])
        lru_cache_model.get_cache_row(2).text_right.become(text_left_right_3[1])
        self.remove(text_left_right_3)
        bits_tag_3 = VGroup(cache_bits_3[0], cache_bits_3[1], cache_bits_3[2])
        tag_text_3, tag_animations_3 = create_cache_tag_bits2table_text_and_animation(
            lru_cache_model, 2, bits_tag_3, "100"
        )
        self.play(tag_animations_3)
        self.wait()
        lru_cache_model.get_cache_row(2).text_tag.become(tag_text_3)
        self.remove(tag_text_3)
        valid_text_3 = Text("1", font_size=30, color=TEAL_B)
        valid_text_3.move_to(
            lru_cache_model.get_cache_row(2).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(lru_cache_model.get_cache_row(2).text_valid, valid_text_3))
        self.wait()
        lru_texts_3, lru_animations_3 = lru_cache_model.increase_lru(2, lru_texts_2)
        self.play(*lru_animations_3)
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_3,
                    memory_bits_3,
                    memory_block_text_3,
                    bits_tag_3,
                    valid_text_3,
                )
            )
        )

        # 处理序列第五行
        self.play(address_sequence.set_row_opacity(3, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(4, 1))
        self.wait()
        (
            cache_bits_4,
            seq2cache_animations_4,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 4
        )
        self.play(*seq2cache_animations_4)
        self.wait()
        (
            memory_bits_4,
            seq2memory_animations_4,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 4
        )
        self.play(*seq2memory_animations_4)
        self.wait()
        memory_block_group_4 = VGroup(
            memory_bits_4[0], memory_bits_4[1], memory_bits_4[2]
        )
        memory_block_text_4 = Text("5", color=RED_D)
        memory_block_text_4.next_to(memory_block_group_4, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_4, memory_block_text_4))
        self.wait()
        self.play(fully_arrow_group[29].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_4,
            memory2cache_animations_4,
        ) = create_memory2cache_text_copy_and_animation(
            memory_model, lru_cache_model, 5, 3
        )
        self.play(*memory2cache_animations_4)
        self.wait()
        lru_cache_model.get_cache_row(3).text_left.become(text_left_right_4[0])
        lru_cache_model.get_cache_row(3).text_right.become(text_left_right_4[1])
        self.remove(text_left_right_4)
        bits_tag_4 = VGroup(cache_bits_4[0], cache_bits_4[1], cache_bits_4[2])
        tag_text_4, tag_animations_4 = create_cache_tag_bits2table_text_and_animation(
            lru_cache_model, 3, bits_tag_4, "101"
        )
        self.play(tag_animations_4)
        self.wait()
        lru_cache_model.get_cache_row(3).text_tag.become(tag_text_4)
        self.remove(tag_text_4)
        valid_text_4 = Text("1", font_size=30, color=TEAL_B)
        valid_text_4.move_to(
            lru_cache_model.get_cache_row(3).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(lru_cache_model.get_cache_row(3).text_valid, valid_text_4))
        self.wait()
        lru_texts_4, lru_animations_4 = lru_cache_model.increase_lru(3, lru_texts_3)
        self.play(*lru_animations_4)
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_4,
                    memory_bits_4,
                    memory_block_text_4,
                    bits_tag_4,
                    valid_text_4,
                )
            )
        )

        # 处理序列第六行
        self.play(address_sequence.set_row_opacity(4, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(5, 1))
        self.wait()
        (
            cache_bits_5,
            seq2cache_animations_5,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 5
        )
        self.play(*seq2cache_animations_5)
        self.wait()
        self.play(Indicate(lru_texts_4[0]))
        self.wait()
        self.play(FlashAround(lru_cache_model.get_cache_row(0)))
        self.wait()
        (
            memory_bits_5,
            seq2memory_animations_5,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 5
        )
        self.play(*seq2memory_animations_5)
        self.wait()
        memory_block_group_5 = VGroup(
            memory_bits_5[0], memory_bits_5[1], memory_bits_5[2]
        )
        memory_block_text_5 = Text("6", color=RED_D)
        memory_block_text_5.next_to(memory_block_group_5, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_5, memory_block_text_5))
        self.wait()
        self.play(fully_arrow_group[0].animate.set_opacity(0.3))
        self.wait()
        self.play(fully_arrow_group[6].animate.set_opacity(1))
        self.wait()
        self.play(
            FadeOut(lru_cache_model.get_cache_row(0).text_left),
            FadeOut(lru_cache_model.get_cache_row(0).text_right),
        )
        self.wait()
        (
            text_left_right_5,
            memory2cache_animations_5,
        ) = create_memory2cache_text_copy_and_animation(
            memory_model, lru_cache_model, 6, 0
        )
        self.play(*memory2cache_animations_5)
        self.wait()
        self.play(FadeOut(lru_cache_model.get_cache_row(0).text_tag))
        self.wait()
        bits_tag_5 = VGroup(cache_bits_5[0], cache_bits_5[1], cache_bits_5[2])
        tag_text_5, tag_animations_5 = create_cache_tag_bits2table_text_and_animation(
            lru_cache_model, 0, bits_tag_5, "110"
        )
        self.play(tag_animations_5)
        self.wait()
        _, lru_animations_5 = lru_cache_model.increase_lru(0, lru_texts_4)
        self.play(*lru_animations_5)
        self.wait()

        self.clear()


class FullMappingDisplayTree(Scene):
    def construct(self) -> None:
        basic_group = VGroup()
        direct_mapping_text = Text("全相联映射").to_edge(UP + LEFT).scale(1.2)
        word_byte_text = (
            Text("1字(Word) = 4字节(Byte)", color=RED)
            .scale(0.7)
            .next_to(direct_mapping_text, DOWN, buff=0.4)
            .align_to(direct_mapping_text, LEFT)
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
        basic_group.add(
            direct_mapping_text, block_word_byte_rect, block_word_byte_group
        )
        memory_model = MemoryModel().shift(RIGHT * 5.4 + DOWN * 0.8)
        memory_bit_table = BitTable(rect_size=0.6)
        memory_bit_table.fill_rects_with_text(
            [
                (0, 3, RED_D, "块索引"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        memory_bit_table.next_to(memory_model, UP, buff=0.5).shift(LEFT * 1.3)
        cache_model = CacheModel(scale_factor=1, show_label=False).shift(
            DOWN * 0.8 + RIGHT * 0.8
        )
        basic_group.add(memory_model, memory_bit_table, cache_model)
        cache_bit_table = BitTable(rect_size=0.6)
        cache_bit_table.fill_rects_with_text(
            [
                (0, 3, PURPLE_B, "标记"),
                (3, 1, YELLOW_D, "块内偏移"),
            ]
        )
        cache_bit_table.next_to(memory_bit_table, LEFT, buff=0.5).shift(LEFT * 1.4)
        fully_arrow_group = VGroup()
        fully_color_set = [RED_B, BLUE_B, GREEN_B, YELLOW_B]
        for i in range(4):
            for j in range(8):
                arrow = Arrow(
                    memory_model.get_memory_row(j).get_left(),
                    cache_model.get_cache_row(i).get_right(),
                    buff=0.05,
                    stroke_color=fully_color_set[i],
                    stroke_width=2,
                ).set_opacity(0.3)
                fully_arrow_group.add(arrow)
        sequence_text = Text("地址序列").scale(0.8)
        sequence_text.next_to(block_word_byte_rect, DOWN, buff=0.5)
        address_sequence = AddressSequence(0, 2, 3, 8, 11, 13)
        address_sequence.next_to(sequence_text, DOWN, buff=0.4)
        for i in range(6):
            address_sequence.get_address_row(i).set_opacity(0.3)
        basic_group.add(
            cache_bit_table, sequence_text, address_sequence, fully_arrow_group
        )
        self.play(FadeIn(basic_group))
        self.wait()

        tree_model = TreeModel(cache_model, scale_factor=1)
        self.play(Write(tree_model))
        self.wait()
        zero_text = Text("0 -> 下", color=GOLD_C)
        one_text = Text("1 -> 上", color=GREEN_C)
        zero_text.next_to(one_text, DOWN, buff=0.2)
        one_zero_group = (
            VGroup(one_text, zero_text).scale(0.8).next_to(tree_model, DOWN)
        )
        self.play(Write(one_zero_group))
        self.wait()

        # 处理序列第一行
        self.play(address_sequence.set_row_opacity(0, 1))
        self.wait()
        (
            cache_bits_0,
            seq2cache_animations_0,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 0
        )
        self.play(*seq2cache_animations_0)
        self.wait()
        (
            memory_bits_0,
            seq2memory_animations_0,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 0
        )
        self.play(*seq2memory_animations_0)
        self.wait()
        memory_block_group_0 = VGroup(
            memory_bits_0[0], memory_bits_0[1], memory_bits_0[2]
        )
        memory_block_text_0 = Text("0", color=RED_D)
        memory_block_text_0.next_to(memory_block_group_0, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_0, memory_block_text_0))
        self.wait()
        self.play(fully_arrow_group[0].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_0,
            memory2cache_animations_0,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 0, 0)
        self.play(*memory2cache_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_left.become(text_left_right_0[0])
        cache_model.get_cache_row(0).text_right.become(text_left_right_0[1])
        self.remove(text_left_right_0)
        bits_tag_0 = VGroup(cache_bits_0[0], cache_bits_0[1], cache_bits_0[2])
        tag_text_0, tag_animations_0 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_0, "000"
        )
        self.play(tag_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_tag.become(tag_text_0)
        self.remove(tag_text_0)
        valid_text_0 = Text("1", font_size=30, color=TEAL_B)
        valid_text_0.move_to(
            cache_model.get_cache_row(0).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(0).text_valid, valid_text_0))
        self.wait()
        tree_model.root_node_label.move_to(tree_model.root_node_rect.get_center())
        tree_model.up_node_label.move_to(tree_model.up_node_rect.get_center())
        tree_model.down_node_label.move_to(tree_model.down_node_rect.get_center())
        root_label_0, animetion_00 = tree_model.create_node_label_animation(
            tree_model.root_node_label, "1"
        )
        self.play(animetion_00)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.root_arrow_up, 1)
        )
        self.wait()
        up_label_0, animetion_01 = tree_model.create_node_label_animation(
            tree_model.up_node_label, "1"
        )
        self.play(animetion_01)
        self.wait()
        self.play(tree_model.create_arrow_opacity_animation(tree_model.up_arrow_up, 1))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_0,
                    memory_bits_0,
                    memory_block_text_0,
                    bits_tag_0,
                    valid_text_0,
                )
            )
        )

        # 处理序列第二行
        self.play(address_sequence.set_row_opacity(0, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(1, 1))
        self.wait()
        (
            cache_bits_1,
            seq2cache_animations_1,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 1
        )
        self.play(*seq2cache_animations_1)
        self.wait()
        (
            memory_bits_1,
            seq2memory_animations_1,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 1
        )
        self.play(*seq2memory_animations_1)
        self.wait()
        memory_block_group_1 = VGroup(
            memory_bits_1[0], memory_bits_1[1], memory_bits_1[2]
        )
        memory_block_text_1 = Text("1", color=RED_D)
        memory_block_text_1.next_to(memory_block_group_1, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_1, memory_block_text_1))
        self.wait()
        self.play(fully_arrow_group[9].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_1,
            memory2cache_animations_1,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 1, 1)
        self.play(*memory2cache_animations_1)
        self.wait()
        cache_model.get_cache_row(1).text_left.become(text_left_right_1[0])
        cache_model.get_cache_row(1).text_right.become(text_left_right_1[1])
        self.remove(text_left_right_1)
        bits_tag_1 = VGroup(cache_bits_1[0], cache_bits_1[1], cache_bits_1[2])
        tag_text_1, tag_animations_1 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 1, bits_tag_1, "001"
        )
        self.play(tag_animations_1)
        self.wait()
        cache_model.get_cache_row(1).text_tag.become(tag_text_1)
        self.remove(tag_text_1)
        valid_text_1 = Text("1", font_size=30, color=TEAL_B)
        valid_text_1.move_to(
            cache_model.get_cache_row(1).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(1).text_valid, valid_text_1))
        self.wait()
        up_label_1, animetion_10 = tree_model.create_node_label_animation(
            up_label_0, "0"
        )
        self.play(animetion_10)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.up_arrow_up, 0.4)
        )
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.up_arrow_down, 1)
        )
        self.wait()
        self.play(FadeOut(VGroup(cache_bits_1, memory_bits_1, memory_block_text_1)))
        self.wait()

        # 处理序列第三行
        self.play(address_sequence.set_row_opacity(1, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(2, 1))
        self.wait()
        (
            cache_bits_2,
            seq2cache_animations_2,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 2
        )
        self.play(*seq2cache_animations_2)
        self.wait()
        self.play(Indicate(tree_model.root_arrow_up))
        self.wait()
        self.play(Indicate(tree_model.up_arrow_down))
        self.wait()
        self.play(FadeOut(VGroup(cache_bits_2)))
        self.wait()

        # 处理序列第四行
        self.play(address_sequence.set_row_opacity(2, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(3, 1))
        self.wait()
        (
            cache_bits_3,
            seq2cache_animations_3,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 3
        )
        self.play(*seq2cache_animations_3)
        self.wait()
        (
            memory_bits_3,
            seq2memory_animations_3,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 3
        )
        self.play(*seq2memory_animations_3)
        self.wait()
        memory_block_group_3 = VGroup(
            memory_bits_3[0], memory_bits_3[1], memory_bits_3[2]
        )
        memory_block_text_3 = Text("4", color=RED_D)
        memory_block_text_3.next_to(memory_block_group_3, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_3, memory_block_text_3))
        self.wait()
        self.play(fully_arrow_group[20].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_3,
            memory2cache_animations_3,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 4, 2)
        self.play(*memory2cache_animations_3)
        self.wait()
        cache_model.get_cache_row(2).text_left.become(text_left_right_3[0])
        cache_model.get_cache_row(2).text_right.become(text_left_right_3[1])
        self.remove(text_left_right_3)
        bits_tag_3 = VGroup(cache_bits_3[0], cache_bits_3[1], cache_bits_3[2])
        tag_text_3, tag_animations_3 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 2, bits_tag_3, "100"
        )
        self.play(tag_animations_3)
        self.wait()
        cache_model.get_cache_row(2).text_tag.become(tag_text_3)
        self.remove(tag_text_3)
        valid_text_3 = Text("1", font_size=30, color=TEAL_B)
        valid_text_3.move_to(
            cache_model.get_cache_row(2).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(2).text_valid, valid_text_3))
        self.wait()
        root_label_3, animetion_30 = tree_model.create_node_label_animation(
            root_label_0, "0"
        )
        self.play(animetion_30)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.root_arrow_up, 0.4)
        )
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.root_arrow_down, 1)
        )
        self.wait()
        down_label_3, animetion_31 = tree_model.create_node_label_animation(
            tree_model.down_node_label, "1"
        )
        self.play(animetion_31)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.down_arrow_up, 1)
        )
        self.wait()
        self.play(FadeOut(VGroup(cache_bits_3, memory_bits_3, memory_block_text_3)))
        self.wait()

        # 处理序列第五行
        self.play(address_sequence.set_row_opacity(3, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(4, 1))
        self.wait()
        (
            cache_bits_4,
            seq2cache_animations_4,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 4
        )
        self.play(*seq2cache_animations_4)
        self.wait()
        (
            memory_bits_4,
            seq2memory_animations_4,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 4
        )
        self.play(*seq2memory_animations_4)
        self.wait()
        memory_block_group_4 = VGroup(
            memory_bits_4[0], memory_bits_4[1], memory_bits_4[2]
        )
        memory_block_text_4 = Text("5", color=RED_D)
        memory_block_text_4.next_to(memory_block_group_4, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_4, memory_block_text_4))
        self.wait()
        self.play(fully_arrow_group[29].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_4,
            memory2cache_animations_4,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 5, 3)
        self.play(*memory2cache_animations_4)
        self.wait()
        cache_model.get_cache_row(3).text_left.become(text_left_right_4[0])
        cache_model.get_cache_row(3).text_right.become(text_left_right_4[1])
        self.remove(text_left_right_4)
        bits_tag_4 = VGroup(cache_bits_4[0], cache_bits_4[1], cache_bits_4[2])
        tag_text_4, tag_animations_4 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 3, bits_tag_4, "101"
        )
        self.play(tag_animations_4)
        self.wait()
        cache_model.get_cache_row(3).text_tag.become(tag_text_4)
        self.remove(tag_text_4)
        valid_text_4 = Text("1", font_size=30, color=TEAL_B)
        valid_text_4.move_to(
            cache_model.get_cache_row(3).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(3).text_valid, valid_text_4))
        self.wait()
        down_label_4, animetion_40 = tree_model.create_node_label_animation(
            down_label_3, "0"
        )
        self.play(animetion_40)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.down_arrow_up, 0.4)
        )
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.down_arrow_down, 1)
        )
        self.wait()
        self.play(FadeOut(VGroup(cache_bits_4, memory_bits_4, memory_block_text_4)))
        self.wait()

        # 处理序列第六行
        self.play(address_sequence.set_row_opacity(4, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(5, 1))
        self.wait()
        (
            cache_bits_5,
            seq2cache_animations_5,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 5
        )
        self.play(*seq2cache_animations_5)
        self.wait()
        root_label_5, animetion_50 = tree_model.create_node_label_animation(
            root_label_3, "1"
        )
        self.play(animetion_50)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.root_arrow_down, 0.4)
        )
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.root_arrow_up, 1)
        )
        self.wait()
        up_label_5, animetion_51 = tree_model.create_node_label_animation(
            up_label_1, "1"
        )
        self.play(animetion_51)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.up_arrow_down, 0.4)
        )
        self.wait()
        self.play(tree_model.create_arrow_opacity_animation(tree_model.up_arrow_up, 1))
        self.wait()
        self.play(FlashAround(cache_model.get_cache_row(0)))
        self.wait()
        (
            memory_bits_5,
            seq2memory_animations_5,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 5
        )
        self.play(*seq2memory_animations_5)
        self.wait()
        memory_block_group_5 = VGroup(
            memory_bits_5[0], memory_bits_5[1], memory_bits_5[2]
        )
        memory_block_text_5 = Text("6", color=RED_D)
        memory_block_text_5.next_to(memory_block_group_5, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_5, memory_block_text_5))
        self.wait()
        self.play(fully_arrow_group[0].animate.set_opacity(0.3))
        self.wait()
        self.play(fully_arrow_group[6].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_5,
            memory2cache_animations_5,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 6, 0)
        self.play(
            FadeOut(cache_model.get_cache_row(0).text_left),
            FadeOut(cache_model.get_cache_row(0).text_right),
        )
        self.wait()
        self.play(*memory2cache_animations_5)
        self.wait()
        self.play(FadeOut(cache_model.get_cache_row(0).text_tag))
        self.wait()
        bits_tag_5 = VGroup(cache_bits_5[0], cache_bits_5[1], cache_bits_5[2])
        tag_text_5, tag_animations_5 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_5, "110"
        )
        self.play(tag_animations_5)
        self.wait()


class SetMappingDisplay(Scene):
    def construct(self) -> None:
        set_mapping_text = Text("2路组相联映射").to_edge(UP + LEFT).scale(1.2)
        word_byte_text = (
            Text("1字(Word) = 4字节(Byte)", color=RED)
            .scale(0.7)
            .next_to(set_mapping_text, DOWN, buff=0.4)
            .align_to(set_mapping_text, LEFT)
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

        self.play(Write(set_mapping_text))
        self.wait()
        self.play(FadeIn(VGroup(block_word_byte_group, block_word_byte_rect)))
        self.wait()

        memory_model = MemoryModel().shift(RIGHT * 5.4 + DOWN * 0.8)
        memory_bit_table = BitTable(rect_size=0.6)
        memory_bit_table.fill_rects_with_text(
            [
                (0, 3, RED_D, "块索引"),
                (3, 1, YELLOW_D, "偏移"),
            ]
        )
        memory_bit_table.next_to(memory_model, UP, buff=0.5).shift(LEFT * 1.3)
        cache_model = LruCacheModel(scale_factor=1).shift(DOWN * 0.8)
        self.play(FadeIn(VGroup(memory_model, memory_bit_table, cache_model)))
        self.wait()
        set_group = cache_model.create_set_rect_and_label()
        self.play(Write(set_group))
        self.wait()
        cache_bit_table = BitTable(rect_size=0.6)
        cache_bit_table.fill_rects_with_text(
            [
                (0, 2, PURPLE_B, "标记"),
                (2, 1, GREEN_B, "组索引"),
                (3, 1, YELLOW_D, "偏移"),
            ]
        )
        cache_bit_table.next_to(memory_bit_table, LEFT, buff=0.5).shift(LEFT * 1.4)
        self.play(Write(cache_bit_table), run_time=2)
        self.wait()
        cache_colors = [BLUE_B, PINK]
        set_arrow_group = VGroup()
        for i in range(8):
            for j in range(2):
                if i % 2 == 0:
                    arrow = Arrow(
                        memory_model.get_memory_row(i).get_left(),
                        cache_model.get_cache_row(j).get_right() + LEFT * 0.1,
                        buff=0.2,
                        stroke_color=cache_colors[0],
                        stroke_width=2,
                    )
                else:
                    arrow = Arrow(
                        memory_model.get_memory_row(i).get_left(),
                        cache_model.get_cache_row(j + 2).get_right() + LEFT * 0.1,
                        buff=0.2,
                        stroke_color=cache_colors[1],
                        stroke_width=2,
                    )
                set_arrow_group.add(arrow)
        self.play(ShowCreation(set_arrow_group))
        self.wait()
        self.play(*[set_arrow_group[i].animate.set_opacity(0.3) for i in range(16)])
        self.wait()

        sequence_text = Text("地址序列").scale(0.8)
        sequence_text.next_to(block_word_byte_rect, DOWN, buff=0.5)

        address_sequence = AddressSequence(0, 2, 3, 8, 11, 13)
        address_sequence.next_to(sequence_text, DOWN, buff=0.4)
        self.play(Write(sequence_text), run_time=2)
        self.wait()
        self.play(Write(address_sequence), run_time=3)
        self.wait()
        self.play(*[address_sequence.set_row_opacity(i, 0.5) for i in range(6)])
        self.wait()

        # 处理序列第一行
        self.play(address_sequence.set_row_opacity(0, 1))
        self.wait()
        (
            cache_bits_0,
            seq2cache_animations_0,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 0
        )
        self.play(*seq2cache_animations_0)
        self.wait()
        set_arrow_0 = CurvedArrow(
            cache_bit_table.get_rect(2).get_bottom(),
            cache_model.set_rect_labels[0].get_top(),
            stroke_color=GREEN_B,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(set_arrow_0))
        self.play(FlashAround(cache_model.set_rects[0]))
        self.wait()
        tag_gruop_0 = VGroup(cache_bits_0[0], cache_bits_0[1])
        self.play(Indicate(tag_gruop_0))
        self.wait()
        cache_model_set0_tag_col = VGroup(
            cache_model.get_cache_row(0).rect_tag,
            cache_model.get_cache_row(1).rect_tag,
        )
        cache_model_set1_tag_col = VGroup(
            cache_model.get_cache_row(2).rect_tag,
            cache_model.get_cache_row(3).rect_tag,
        )
        cache_model_set0_valid_col = VGroup(
            cache_model.get_cache_row(0).rect_valid,
            cache_model.get_cache_row(1).rect_valid,
        )
        cache_model_set1_valid_col = VGroup(
            cache_model.get_cache_row(2).rect_valid,
            cache_model.get_cache_row(3).rect_valid,
        )
        self.play(
            FlashAround(cache_model_set0_tag_col),
            FlashAround(cache_model_set0_valid_col),
            run_time=2,
        )
        self.wait()
        (
            memory_bits_0,
            seq2memory_animations_0,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 0
        )
        self.play(*seq2memory_animations_0)
        self.wait()
        memory_block_group_0 = VGroup(
            memory_bits_0[0], memory_bits_0[1], memory_bits_0[2]
        )
        memory_block_text_0 = Text("0", color=RED_D)
        memory_block_text_0.next_to(memory_block_group_0, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_0, memory_block_text_0))
        self.wait()
        block_arrow_0 = CurvedArrow(
            memory_block_text_0.get_bottom(),
            memory_model.get_memory_row(0).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_0))
        self.play(FlashAround(memory_model.get_memory_row(0)))
        self.play(FadeOut(block_arrow_0))
        self.wait()
        self.play(set_arrow_group[0].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_0,
            memory2cache_animations_0,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 0, 0)
        self.play(*memory2cache_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_left.become(text_left_right_0[0])
        cache_model.get_cache_row(0).text_right.become(text_left_right_0[1])
        self.remove(text_left_right_0)
        bits_tag_0 = VGroup(cache_bits_0[0], cache_bits_0[1])
        tag_text_0, tag_animations_0 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_0, "00"
        )
        self.play(tag_animations_0)
        self.wait()
        cache_model.get_cache_row(0).text_tag.become(tag_text_0)
        self.remove(tag_text_0)
        valid_text_0 = Text("1", font_size=30, color=TEAL_B)
        valid_text_0.move_to(
            cache_model.get_cache_row(0).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(0).text_valid, valid_text_0))
        self.wait()
        init_set0_lru_list = []
        init_set1_lru_list = []
        for i in range(2):
            init_set0_lru_list.append(cache_model.get_cache_row(i).text_lru)
            init_set1_lru_list.append(cache_model.get_cache_row(i + 2).text_lru)
        new_set0_texts_0, set0_lru_animations_0 = cache_model.increase_lru(
            0, init_set0_lru_list, set_index=0
        )
        self.play(*set0_lru_animations_0)
        self.wait()
        offset_arrow_0 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(0).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_0))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_0,
                    memory_bits_0,
                    memory_block_text_0,
                    offset_arrow_0,
                    set_arrow_0,
                )
            )
        )
        self.wait()

        # 处理序列第二行
        self.play(address_sequence.set_row_opacity(0, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(1, 1))
        self.wait()
        (
            cache_bits_1,
            seq2cache_animations_1,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 1
        )
        self.play(*seq2cache_animations_1)
        self.wait()
        set_arrow_1 = CurvedArrow(
            cache_bit_table.get_rect(2).get_bottom(),
            cache_model.set_rect_labels[1].get_top(),
            stroke_color=GREEN_B,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(set_arrow_1))
        self.play(FlashAround(cache_model.set_rects[1]))
        self.wait()
        tag_gruop_1 = VGroup(cache_bits_1[0], cache_bits_1[1])
        self.play(Indicate(tag_gruop_1))
        self.wait()
        self.play(
            FlashAround(cache_model_set1_tag_col),
            FlashAround(cache_model_set1_valid_col),
            run_time=2,
        )
        self.wait()
        (
            memory_bits_1,
            seq2memory_animations_1,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 1
        )
        self.play(*seq2memory_animations_1)
        self.wait()
        memory_block_group_1 = VGroup(
            memory_bits_1[0], memory_bits_1[1], memory_bits_1[2]
        )
        memory_block_text_1 = Text("1", color=RED_D)
        memory_block_text_1.next_to(memory_block_group_1, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_1, memory_block_text_1))
        self.wait()
        block_arrow_1 = CurvedArrow(
            memory_block_text_1.get_bottom(),
            memory_model.get_memory_row(1).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_1))
        self.play(FlashAround(memory_model.get_memory_row(1)))
        self.play(FadeOut(block_arrow_1))
        self.wait()
        self.play(set_arrow_group[2].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_1,
            memory2cache_animations_1,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 1, 2)
        self.play(*memory2cache_animations_1)
        self.wait()
        cache_model.get_cache_row(2).text_left.become(text_left_right_1[0])
        cache_model.get_cache_row(2).text_right.become(text_left_right_1[1])
        self.remove(text_left_right_1)
        bits_tag_1 = VGroup(cache_bits_1[0], cache_bits_1[1])
        tag_text_1, tag_animations_1 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 2, bits_tag_1, "00"
        )
        self.play(tag_animations_1)
        self.wait()
        cache_model.get_cache_row(2).text_tag.become(tag_text_1)
        self.remove(tag_text_1)
        valid_text_1 = Text("1", font_size=30, color=TEAL_B)
        valid_text_1.move_to(
            cache_model.get_cache_row(2).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(2).text_valid, valid_text_1))
        self.wait()
        new_set1_texts_1, set1_lru_animations_1 = cache_model.increase_lru(
            0, init_set1_lru_list, set_index=1
        )
        self.play(*set1_lru_animations_1)
        self.wait()
        offset_arrow_1 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(2).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_1))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(2).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_1,
                    memory_bits_1,
                    memory_block_text_1,
                    offset_arrow_1,
                    set_arrow_1,
                )
            )
        )
        self.wait()

        # 处理序列第三行
        self.play(address_sequence.set_row_opacity(1, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(2, 1))
        self.wait()
        (
            cache_bits_2,
            seq2cache_animations_2,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 2
        )
        self.play(*seq2cache_animations_2)
        self.wait()
        set_arrow_2 = CurvedArrow(
            cache_bit_table.get_rect(2).get_bottom(),
            cache_model.set_rect_labels[1].get_top(),
            stroke_color=GREEN_B,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(set_arrow_2))
        self.play(FlashAround(cache_model.set_rects[1]))
        self.wait()
        tag_gruop_2 = VGroup(cache_bits_2[0], cache_bits_2[1])
        self.play(Indicate(tag_gruop_2))
        self.wait()
        self.play(
            Indicate(cache_model.get_cache_row(2).text_tag),
            Indicate(cache_model.get_cache_row(2).text_valid),
        )
        self.wait()
        new_set1_texts_2, set1_lru_animations_2 = cache_model.increase_lru(
            0, new_set1_texts_1, set_index=1
        )
        self.play(*set1_lru_animations_2)
        self.wait()
        offset_arrow_2 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(2).text_right.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_2))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(2).text_right))
        self.wait()
        self.play(FadeOut(VGroup(cache_bits_2, offset_arrow_2, set_arrow_2)))
        self.wait()

        # 处理序列第四行
        self.play(address_sequence.set_row_opacity(2, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(3, 1))
        self.wait()
        (
            cache_bits_3,
            seq2cache_animations_3,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 3
        )
        self.play(*seq2cache_animations_3)
        self.wait()
        set_arrow_3 = CurvedArrow(
            cache_bit_table.get_rect(2).get_bottom(),
            cache_model.set_rect_labels[0].get_top(),
            stroke_color=GREEN_B,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(set_arrow_3))
        self.play(FlashAround(cache_model.set_rects[0]))
        self.wait()
        tag_gruop_3 = VGroup(cache_bits_3[0], cache_bits_3[1])
        self.play(Indicate(tag_gruop_3))
        self.wait()
        self.play(
            FlashAround(cache_model_set0_tag_col),
            FlashAround(cache_model_set0_valid_col),
            run_time=2,
        )
        self.wait()
        (
            memory_bits_3,
            seq2memory_animations_3,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 3
        )
        self.play(*seq2memory_animations_3)
        self.wait()
        memory_block_group_3 = VGroup(
            memory_bits_3[0], memory_bits_3[1], memory_bits_3[2]
        )
        memory_block_text_3 = Text("4", color=RED_D)
        memory_block_text_3.next_to(memory_block_group_3, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_3, memory_block_text_3))
        self.wait()
        block_arrow_3 = CurvedArrow(
            memory_block_text_3.get_bottom(),
            memory_model.get_memory_row(4).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_3))
        self.play(FlashAround(memory_model.get_memory_row(4)))
        self.play(FadeOut(block_arrow_3))
        self.wait()
        self.play(set_arrow_group[9].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_3,
            memory2cache_animations_3,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 4, 1)
        self.play(*memory2cache_animations_3)
        self.wait()
        cache_model.get_cache_row(1).text_left.become(text_left_right_3[0])
        cache_model.get_cache_row(1).text_right.become(text_left_right_3[1])
        self.remove(text_left_right_3)
        bits_tag_3 = VGroup(cache_bits_3[0], cache_bits_3[1])
        tag_text_3, tag_animations_3 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 1, bits_tag_3, "10"
        )
        self.play(tag_animations_3)
        self.wait()
        cache_model.get_cache_row(1).text_tag.become(tag_text_3)
        self.remove(tag_text_3)
        valid_text_3 = Text("1", font_size=30, color=TEAL_B)
        valid_text_3.move_to(
            cache_model.get_cache_row(1).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(1).text_valid, valid_text_3))
        self.wait()
        new_set0_texts_3, set0_lru_animations_3 = cache_model.increase_lru(
            1, new_set0_texts_0, set_index=0
        )
        self.play(*set0_lru_animations_3)
        self.wait()
        offset_arrow_3 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(1).text_left.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_3))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(1).text_left))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_3,
                    memory_bits_3,
                    memory_block_text_3,
                    offset_arrow_3,
                    set_arrow_3,
                )
            )
        )
        self.wait()

        # 处理序列第五行
        self.play(address_sequence.set_row_opacity(3, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(4, 1))
        self.wait()
        (
            cache_bits_4,
            seq2cache_animations_4,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 4
        )
        self.play(*seq2cache_animations_4)
        self.wait()
        set_arrow_4 = CurvedArrow(
            cache_bit_table.get_rect(2).get_bottom(),
            cache_model.set_rect_labels[1].get_top(),
            stroke_color=GREEN_B,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(set_arrow_4))
        self.play(FlashAround(cache_model.set_rects[1]))
        self.wait()
        tag_gruop_4 = VGroup(cache_bits_4[0], cache_bits_4[1])
        self.play(Indicate(tag_gruop_4))
        self.wait()
        self.play(
            FlashAround(cache_model_set1_tag_col),
            FlashAround(cache_model_set1_valid_col),
            run_time=2,
        )
        self.wait()
        (
            memory_bits_4,
            seq2memory_animations_4,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 4
        )
        self.play(*seq2memory_animations_4)
        self.wait()
        memory_block_group_4 = VGroup(
            memory_bits_4[0], memory_bits_4[1], memory_bits_4[2]
        )
        memory_block_text_4 = Text("5", color=RED_D)
        memory_block_text_4.next_to(memory_block_group_4, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_4, memory_block_text_4))
        self.wait()
        block_arrow_4 = CurvedArrow(
            memory_block_text_4.get_bottom(),
            memory_model.get_memory_row(5).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_4))
        self.play(FlashAround(memory_model.get_memory_row(5)))
        self.play(FadeOut(block_arrow_4))
        self.wait()
        self.play(set_arrow_group[11].animate.set_opacity(1))
        self.wait()
        (
            text_left_right_4,
            memory2cache_animations_4,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 5, 3)
        self.play(*memory2cache_animations_4)
        self.wait()
        cache_model.get_cache_row(3).text_left.become(text_left_right_4[0])
        cache_model.get_cache_row(3).text_right.become(text_left_right_4[1])
        self.remove(text_left_right_4)
        bits_tag_4 = VGroup(cache_bits_4[0], cache_bits_4[1])
        tag_text_4, tag_animations_4 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 3, bits_tag_4, "10"
        )
        self.play(tag_animations_4)
        self.wait()
        cache_model.get_cache_row(3).text_tag.become(tag_text_4)
        self.remove(tag_text_4)
        valid_text_4 = Text("1", font_size=30, color=TEAL_B)
        valid_text_4.move_to(
            cache_model.get_cache_row(3).text_valid.get_center()
        ).shift(LEFT * 0.02)
        self.play(Transform(cache_model.get_cache_row(3).text_valid, valid_text_4))
        self.wait()
        new_set1_texts_4, set1_lru_animations_4 = cache_model.increase_lru(
            1, new_set1_texts_2, set_index=1
        )
        self.play(*set1_lru_animations_4)
        self.wait()
        offset_arrow_4 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(3).text_right.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_4))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(3).text_right))
        self.wait()
        self.play(
            FadeOut(
                VGroup(
                    cache_bits_4,
                    memory_bits_4,
                    memory_block_text_4,
                    offset_arrow_4,
                    set_arrow_4,
                )
            )
        )
        self.wait()

        # 处理序列第六行
        self.play(address_sequence.set_row_opacity(4, 0.5))
        self.wait()
        self.play(address_sequence.set_row_opacity(5, 1))
        self.wait()
        (
            cache_bits_5,
            seq2cache_animations_5,
        ) = create_seq2cache_bit_text_copy_and_animation(
            address_sequence, cache_bit_table, 5
        )
        self.play(*seq2cache_animations_5)
        self.wait()
        set_arrow_5 = CurvedArrow(
            cache_bit_table.get_rect(2).get_bottom(),
            cache_model.set_rect_labels[0].get_top(),
            stroke_color=GREEN_B,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(set_arrow_5))
        self.play(FlashAround(cache_model.set_rects[0]))
        self.wait()
        tag_gruop_5 = VGroup(cache_bits_5[0], cache_bits_5[1])
        self.play(Indicate(tag_gruop_5))
        self.wait()
        self.play(
            FlashAround(cache_model_set0_tag_col),
            FlashAround(cache_model_set0_valid_col),
            run_time=2,
        )
        self.wait()
        self.play(Indicate(new_set0_texts_3[0]))
        self.wait()
        (
            memory_bits_5,
            seq2memory_animations_5,
        ) = create_seq2memory_bit_text_copy_and_animation(
            address_sequence, memory_bit_table, 5
        )
        self.play(*seq2memory_animations_5)
        self.wait()
        memory_block_group_5 = VGroup(
            memory_bits_5[0], memory_bits_5[1], memory_bits_5[2]
        )
        memory_block_text_5 = Text("6", color=RED_D)
        memory_block_text_5.next_to(memory_block_group_5, DOWN, buff=0.3)
        self.play(TransformFromCopy(memory_block_group_5, memory_block_text_5))
        self.wait()
        block_arrow_5 = CurvedArrow(
            memory_block_text_5.get_bottom(),
            memory_model.get_memory_row(6).get_left(),
            stroke_color=RED_D,
            stroke_width=3,
            angle=TAU / 4,
        )
        self.play(ShowCreation(block_arrow_5))
        self.play(FlashAround(memory_model.get_memory_row(6)))
        self.play(FadeOut(block_arrow_5))
        self.wait()
        self.play(set_arrow_group[0].animate.set_opacity(0.3))
        self.wait()
        self.play(set_arrow_group[12].animate.set_opacity(1))
        self.wait()
        self.play(
            FadeOut(cache_model.get_cache_row(0).text_left),
            FadeOut(cache_model.get_cache_row(0).text_right),
        )
        self.wait()
        (
            text_left_right_5,
            memory2cache_animations_5,
        ) = create_memory2cache_text_copy_and_animation(memory_model, cache_model, 6, 0)
        self.play(*memory2cache_animations_5)
        self.wait()
        bits_tag_5 = VGroup(cache_bits_5[0], cache_bits_5[1])
        tag_text_5, tag_animations_5 = create_cache_tag_bits2table_text_and_animation(
            cache_model, 0, bits_tag_5, "11"
        )
        self.play(FadeOut(cache_model.get_cache_row(0).text_tag))
        self.wait()
        self.play(tag_animations_5)
        self.wait()
        new_set0_texts_5, set0_lru_animations_5 = cache_model.increase_lru(
            0, new_set0_texts_3, set_index=0
        )
        self.play(*set0_lru_animations_5)
        self.wait()
        offset_arrow_5 = Arrow(
            cache_bit_table.get_rect(3).get_bottom(),
            cache_model.get_cache_row(0).text_right.get_top(),
            stroke_color=YELLOW_D,
            stroke_width=4,
        )
        self.play(ShowCreation(offset_arrow_5))
        self.wait()
        self.play(Indicate(text_left_right_5[1]))
        self.wait()


class Cache2Cover(Scene):
    def construct(self) -> None:
        title = (
            Text("Cache运作原理", color=YELLOW)
            .scale(3)
            .to_edge(UL, buff=0.8)
            .shift(RIGHT * 0.2)
        )

        trick = (
            Text(
                """
                     三种映射

                     替换策略

                     伪LRU
                     """,
                color=LIGHT_PINK,
            )
            .scale(1.2)
            .to_edge(DR, buff=0.8)
            .shift(LEFT * 2 + UP * 0.6)
        )
        group = VGroup(title, trick)
        group.scale(1).shift(RIGHT * 1.2)
        self.add(title)
        self.add(trick)


class TestAddSeq(Scene):
    def construct(self) -> None:
        title = Text("Cache", color=WHITE).scale(1.5)

        addressSequence = AddressSequence(0, 2, 3, 8)
        self.play(Write(addressSequence), run_time=3)
        self.wait()
        self.play(*[addressSequence.set_row_opacity(i, 0.5) for i in range(4)])
        self.wait()
        self.play(addressSequence.set_row_opacity(0, 1))
        self.wait()


class TestCacheModel(Scene):
    def construct(self) -> None:
        cache_model = CacheModel()
        self.play(Write(cache_model), run_time=3)
        self.wait()
        self.play(FlashAround(cache_model.get_cache_row(0).text_left))
        self.wait()
        text = Text("0", color=RED_D)
        text.move_to(cache_model.get_cache_row(0).rect_left.get_center())
        cache_model.get_cache_row(0).text_left.become(text)
        self.play(Write(text))
        self.wait()
        self.play(Indicate(cache_model.get_cache_row(0).text_left))
        self.wait()


class TestLruCacheModel(Scene):
    def construct(self) -> None:
        lru_cache_model = LruCacheModel()
        self.play(Write(lru_cache_model), run_time=1)
        self.wait()
        init_lru_list = []
        for i in range(4):
            init_lru_list.append(lru_cache_model.get_cache_row(i).text_lru)
        new_texts, lru_animations = lru_cache_model.increase_lru(0, init_lru_list)
        self.play(*lru_animations)
        self.wait()
        new_texts2, lru_animations2 = lru_cache_model.increase_lru(1, new_texts)
        self.play(*lru_animations2)
        self.wait()
        new_texts3, lru_animations3 = lru_cache_model.increase_lru(1, new_texts2)
        self.play(*lru_animations3)
        self.wait()


class TestBit(Scene):
    def construct(self):
        rects_group = BitTable(rect_size=0.6)

        # rects_group.fill_rects_with_text([
        #     (0, 1, PURPLE, "标记"),
        #     (1, 2, GREEN, "索引"),
        #     (3, 1, YELLOW, "偏移量"),
        # ])

        rects_group.fill_rects_with_text(
            [
                (0, 3, PURPLE, "标记"),
                (3, 1, YELLOW, "偏移量"),
            ]
        )

        self.add(rects_group)


class TestTreeCacheModel(Scene):
    def construct(self) -> None:
        cache_model = CacheModel(scale_factor=1, show_label=False).shift(
            DOWN * 0.8 + RIGHT * 0.8
        )
        tree_model = TreeModel(cache_model, scale_factor=1)
        self.add(cache_model, tree_model)
        label1, animation1 = tree_model.create_node_label_animation(
            tree_model.root_node_label, "1"
        )
        self.play(animation1)
        self.wait()
        self.play(
            tree_model.create_arrow_opacity_animation(tree_model.root_arrow_up, 1)
        )
        self.wait()


class TestSetLruCacheModel(Scene):
    def construct(self) -> None:
        set_lru_model = LruCacheModel()
        self.play(Write(set_lru_model), run_time=1)
        self.wait()
        init_set0_lru_list = []
        init_set1_lru_list = []
        for i in range(2):
            init_set0_lru_list.append(set_lru_model.get_cache_row(i).text_lru)
            init_set1_lru_list.append(set_lru_model.get_cache_row(i + 2).text_lru)
        new_set0_texts, set0_lru_animations = set_lru_model.increase_lru(
            0, init_set0_lru_list, set_index=0
        )
        self.play(*set0_lru_animations)
        self.wait()
        new_set0_texts2, set0_lru_animations2 = set_lru_model.increase_lru(
            1, new_set0_texts, set_index=0
        )
        self.play(*set0_lru_animations2)
        self.wait()
        new_set1_texts, set1_lru_animations = set_lru_model.increase_lru(
            0, init_set1_lru_list, set_index=1
        )
        self.play(*set1_lru_animations)
        self.wait()
        new_set1_texts2, set1_lru_animations2 = set_lru_model.increase_lru(
            1, new_set1_texts, set_index=1
        )
        self.play(*set1_lru_animations2)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    # TestModel DirectMappingDisplay FullMappingDisplay 
    command = f"manimgl {module_name} Cache2Cover -s -ow"
    os.system(command)
