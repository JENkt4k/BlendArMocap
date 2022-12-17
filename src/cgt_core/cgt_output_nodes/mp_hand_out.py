'''
Copyright (C) cgtinker, cgtinker.com, hello@cgtinker.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import annotations
from . import mp_out_utils
from ..cgt_naming import COLLECTIONS
from ..cgt_bpy import cgt_bpy_utils, cgt_collection
from ..cgt_utils import cgt_json
from pathlib import Path


class CgtMPHandOutNode(mp_out_utils.BpyOutputNode):
    left_hand = []
    right_hand = []
    col_name = COLLECTIONS.hands
    parent_col = COLLECTIONS.drivers

    def __init__(self):
        path = Path(__file__).parent / "data/hand.json"
        data = cgt_json.JsonData(str(path))
        references = data()
        self.left_hand = cgt_bpy_utils.add_empties(references, 0.005, prefix=".L", suffix="cgt_")
        self.right_hand = cgt_bpy_utils.add_empties(references, 0.005, prefix=".R", suffix="cgt_")
        cgt_collection.add_list_to_collection(self.col_name, self.left_hand, self.parent_col)
        cgt_collection.add_list_to_collection(self.col_name, self.right_hand, self.parent_col)

    def split(self, data):
        left_hand_data, right_hand_data = data
        return [[self.left_hand, left_hand_data], [self.right_hand, right_hand_data]]

    def update(self, data, frame):
        loc, rot, sca = data
        for data, method in zip([loc, rot, sca], [self.translate, self.euler_rotate, self.scale]):
            for hand, chunk in self.split(data):
                try:
                    method(hand, chunk, frame)
                except IndexError:
                    pass
        return data, frame
