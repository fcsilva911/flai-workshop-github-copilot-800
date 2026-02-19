import React from 'react';
import { Routes, Route, NavLink } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

const features = [
  { to: '/users',       icon: '👤', title: 'Users',       text: 'Manage athlete profiles and accounts.'     },
  { to: '/teams',       icon: '🏆', title: 'Teams',       text: 'Create and manage competitive teams.'      },
  { to: '/activities',  icon: '🏃', title: 'Activities',  text: 'Log and review fitness activities.'        },
  { to: '/leaderboard', icon: '📊', title: 'Leaderboard', text: 'See who is leading the pack.'              },
  { to: '/workouts',    icon: '💪', title: 'Workouts',    text: 'Browse personalised workout plans.'        },
];

function App() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            OctoFit Tracker
          </NavLink>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              {features.map((f) => (
                <li className="nav-item" key={f.to}>
                  <NavLink
                    className={({ isActive }) => 'nav-link' + (isActive ? ' active' : '')}
                    to={f.to}
                  >
                    {f.title}
                  </NavLink>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-3">
        <Routes>
          <Route
            path="/"
            element={
              <>
                <div className="octofit-hero">
                  <h1 className="display-5 fw-bold">Welcome to OctoFit Tracker</h1>
                  <p className="lead">
                    Track your fitness activities, workouts, and compete on the leaderboard.
                  </p>
                  <hr className="border-secondary my-4" />
                  <p className="mb-4">
                    Use the navigation menu above to explore Users, Teams, Activities, Leaderboard, and Workouts.
                  </p>
                  <NavLink to="/activities" className="btn btn-outline-light me-2">
                    Log Activity
                  </NavLink>
                  <NavLink to="/leaderboard" className="btn btn-primary">
                    View Leaderboard
                  </NavLink>
                </div>

                <div className="row g-3 mt-2 mb-4">
                  {features.map((f) => (
                    <div className="col-12 col-sm-6 col-lg-4" key={f.to}>
                      <NavLink to={f.to} className="card octofit-feature-card h-100 p-3">
                        <div className="card-body">
                          <div className="fs-2 mb-2">{f.icon}</div>
                          <h5 className="card-title">{f.title}</h5>
                          <p className="card-text text-muted small">{f.text}</p>
                        </div>
                      </NavLink>
                    </div>
                  ))}
                </div>
              </>
            }
          />
          <Route path="/users"       element={<Users />}       />
          <Route path="/teams"       element={<Teams />}       />
          <Route path="/activities"  element={<Activities />}  />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts"    element={<Workouts />}    />
        </Routes>
      </div>
    </div>
  );
}

export default App;
