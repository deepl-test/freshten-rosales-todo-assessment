export interface Task {
    id: number;
    name: string;
    description: string;
    completed: boolean;
    due_date: string | null;
    completed_date: string | null;
    created_at: string;
    updated_at: string;
  }
  
  export type CreateTaskData = Omit<Task, 'id' | 'completed_date' | 'created_at' | 'updated_at'>;
  export type UpdateTaskData = Partial<CreateTaskData>;