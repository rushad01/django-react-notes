import { createSlice } from "@reduxjs/toolkit";
import { fetchLanguages } from "../thunks/fetchLanguages";

const languagesSlice = createSlice({
  name: "language",
  initialState: {
    isLoading: false,
    data: [],
    error: null,
  },
  reducers: {},
  extraReducers(builder) {
    builder.addCase(fetchLanguages.pending, (state, action) => {
      state.isLoading = true;
    });
    builder.addCase(fetchLanguages.fulfilled, (state, action) => {
      state.isLoading = false;
      state.data = action.payload;
    });
    builder.addCase(fetchLanguages.rejected, (state, action) => {
      state.isLoading = false;
      state.error = action.error;
    });
  },
});

export const languagesReducer = languagesSlice.reducer;
