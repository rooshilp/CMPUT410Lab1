# Copyright 2015 Rooshil Patel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Student:
    courseMarks = {}
    name=""
    
    def __init__(self, name, family):
        self.name = name + " " + family
        
        
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        average = 0
        for key in self.courseMarks:
            average += self.courseMarks[key]
        if (average != 0) and (len(self.courseMarks) != 0):
            average = average/len(self.courseMarks)
        return average
    
def main():
    guy = Student("guy", "one")
    guy.addCourseMark("math", 90)
    guy.addCourseMark("math2", 80)
    guy.addCourseMark("math3", 90)
    guy.addCourseMark("math4", 80)
    guy.addCourseMark("math5", 95)
    print(guy.average())
    print(guy.name)
    print(guy.courseMarks)
    
main()
