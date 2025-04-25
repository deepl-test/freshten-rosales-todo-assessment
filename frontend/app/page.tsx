import TaskList from '@/components/TaskList';
import AddTaskForm from '@/components/AddTaskForm';

export default function Home() {
  return (
    <main className="mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold mb-8">Task Manager</h1>
      <AddTaskForm />
      <TaskList />
    </main>
  );
}