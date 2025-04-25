"use client";
import { useTasks, useDeleteTask, useUpdateTask } from '../hooks/useTasks';
import { Task } from '../types/task';
import { PencilIcon, TrashIcon, CheckIcon } from '@heroicons/react/24/outline';
import { useState } from 'react';

export default function TaskList() {
  const { data: tasks, isLoading, error } = useTasks();
  const deleteTaskMutation = useDeleteTask();
  const updateTaskMutation = useUpdateTask();
  const [editingTaskId, setEditingTaskId] = useState<number | null>(null);
  const [editedName, setEditedName] = useState('');
  const [editedDescription, setEditedDescription] = useState('');

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading tasks</div>;

  const handleEdit = (task: Task) => {
    setEditingTaskId(task.id);
    setEditedName(task.name);
    setEditedDescription(task.description || '');
  };

  const handleSave = (taskId: number) => {
    updateTaskMutation.mutate({
      id: taskId,
      name: editedName,
      description: editedDescription,
    });
    setEditingTaskId(null);
  };

  const toggleComplete = (task: Task) => {
    updateTaskMutation.mutate({
      id: task.id,
      completed: !task.completed,
    });
  };

  return (
    <div className="space-y-4">
      {tasks?.map((task) => (
        <div
          key={task.id}
          className={`p-4 border rounded-lg ${task.completed ? 'bg-gray-50' : 'bg-white'}`}
        >
          {editingTaskId === task.id ? (
            <div className="space-y-2">
              <input
                type="text"
                value={editedName}
                onChange={(e) => setEditedName(e.target.value)}
                className="w-full p-2 border rounded"
              />
              <textarea
                value={editedDescription}
                onChange={(e) => setEditedDescription(e.target.value)}
                className="w-full p-2 border rounded"
              />
              <button
                onClick={() => handleSave(task.id)}
                className="px-4 py-2 bg-primary-500 text-white rounded"
              >
                Save
              </button>
            </div>
          ) : (
            <div className="flex justify-between items-start">
              <div className="flex items-start space-x-3">
                <button onClick={() => toggleComplete(task)}>
                  <div
                    className={`w-6 h-6 rounded-full border flex items-center justify-center ${
                      task.completed
                        ? 'bg-primary-500 border-primary-500'
                        : 'border-gray-300'
                    }`}
                  >
                    {task.completed && (
                      <CheckIcon className="w-4 h-4 text-white" />
                    )}
                  </div>
                </button>
                <div>
                  <h3
                    className={`font-medium ${
                      task.completed ? 'line-through text-gray-500' : ''
                    }`}
                  >
                    {task.name}
                  </h3>
                  {task.description && (
                    <p className="text-gray-600">{task.description}</p>
                  )}
                  {task.due_date && (
                    <p className="text-sm text-gray-500">
                      Due: {new Date(task.due_date).toLocaleString()}
                    </p>
                  )}
                </div>
              </div>
              <div className="flex space-x-2">
                <button
                  onClick={() => handleEdit(task)}
                  className="text-gray-500 hover:text-primary-500"
                >
                  <PencilIcon className="w-5 h-5" />
                </button>
                <button
                  onClick={() => deleteTaskMutation.mutate(task.id)}
                  className="text-gray-500 hover:text-red-500"
                >
                  <TrashIcon className="w-5 h-5" />
                </button>
              </div>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}