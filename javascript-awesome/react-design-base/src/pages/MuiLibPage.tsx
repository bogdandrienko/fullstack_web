import React from "react";
import { AppBar, IconButton, Toolbar, Typography } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";

export default function Page() {
  return (
    <div>
      <AppBar position="static">
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <DeleteIcon />
          </IconButton>
          <Typography variant="h6" color="inherit" component="div">
            Photos
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}
