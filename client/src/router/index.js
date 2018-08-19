import Vue from 'vue'
import Router from 'vue-router'
import Student from '@/components/Student'
import Grade from '@/components/Grade'
import StudentGrade from '@/components/StudentGrade'
import Professor from '@/components/Professor'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Student',
      component: Student
    },
    {
      path: '/grades',
      name: 'Grade',
      component: Grade
    },
    {
      path: '/student/:id/grades',
      name: 'StudentGrade',
      component: StudentGrade
    },
     {
      path: '/professors',
      name: 'Professor',
      component: Professor
    }
  ]
})
