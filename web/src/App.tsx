import { Routes, Route, BrowserRouter } from "react-router-dom";
import logo from "./logo.svg";
import "./App.css";
import { withLayout } from "./Layout";
import MoviesPage from "./pages/movies";

function App() {
  return (
    <div className="App">
      <header className="App-header"></header>
      <Routes>
        <Route path="/" element={withLayout(<MoviesPage />)} />
      </Routes>
    </div>
  );
}

export default App;
