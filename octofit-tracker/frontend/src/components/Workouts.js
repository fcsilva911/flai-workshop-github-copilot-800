import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Workouts: fetched data', data);
        // Support both paginated (.results) and plain array responses
        const items = Array.isArray(data) ? data : data.results || [];
        setWorkouts(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Workouts: fetch error', err);
        setError(err.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) return (
    <div className="octofit-spinner-wrapper">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
    </div>
  );

  if (error) return (
    <div className="alert alert-danger mt-4" role="alert">
      <strong>Error:</strong> {error}
    </div>
  );

  const difficultyBadge = (difficulty) => {
    const level = (difficulty || '').toLowerCase();
    if (level === 'easy')   return 'badge bg-success';
    if (level === 'medium') return 'badge bg-warning text-dark';
    if (level === 'hard')   return 'badge bg-danger';
    return 'badge bg-secondary';
  };

  return (
    <div className="card octofit-card mt-4">
      <div className="card-header bg-dark text-white">
        <h2 className="h4 mb-0">Workouts</h2>
      </div>
      <div className="card-body p-0">
        {workouts.length === 0 ? (
          <p className="text-muted p-3 mb-0">No workouts found.</p>
        ) : (
          <div className="table-responsive">
            <table className="table table-hover table-striped mb-0">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Category</th>
                  <th>Difficulty</th>
                  <th>Duration (min)</th>
                  <th>Calories/Session</th>
                  <th>Description</th>
                </tr>
              </thead>
              <tbody>
                {workouts.map((workout, index) => (
                  <tr key={workout._id || index}>
                    <td><strong>{workout.name}</strong></td>
                    <td><span className="badge bg-info text-dark">{workout.category}</span></td>
                    <td><span className={difficultyBadge(workout.difficulty)}>{workout.difficulty}</span></td>
                    <td>{workout.duration}</td>
                    <td>{workout.calories_per_session}</td>
                    <td>{workout.description}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;
