import { createAsyncThunk } from "@reduxjs/toolkit";
import { api } from "../../api/notes";

const fetchNotes = createAsyncThunk("notes/fetch", async () => {
  const response = await api.get("/notes/", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  return response.data;
});

export { fetchNotes };
