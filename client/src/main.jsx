import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

// import components for routes
import Home from './components/Home.jsx'
import App from './components/App.jsx'
import ErrorElement from './components/ErrorElement.jsx';
import Login from './components/Login.jsx';
import './index.css'

// createRoot(document.getElementById('root')).render(
//   <StrictMode>
//     <App />
//   </StrictMode>,
// )

// create router. Defines paths and elements rendered by paths
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorElement />,
    children: [
      {
        path: "/",
        element: <Home />
      },
      {
        path: "/login",
        element: <Login />
      }
    ]
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(<RouterProvider router={router} />);

