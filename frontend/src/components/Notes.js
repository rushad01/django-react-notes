import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchNotes } from "../store/thunks/fetchNotes";

function Notes() {
  const dispatch = useDispatch();
  const { isLoading, data, error } = useSelector((state) => {
    return state.notes;
  });

  useEffect(() => {
    dispatch(fetchNotes());
  }, [dispatch]);

  if (isLoading) {
    return <div>Notes are Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }
  const renderNotes = data.map((note) => {
    return (
      <div key={note.id}>
        <h4>Title:{note.title}</h4>
        <p>Programming Language:{note.language}</p>
        <p>Catagory: {note.catagory}</p>
        <p>Note: {note.note}</p>
      </div>
    );
  });
  return <div>{renderNotes}</div>;
}

export default Notes;
