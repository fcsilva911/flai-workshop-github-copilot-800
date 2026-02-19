import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Activities: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Activities: fetched data', data);
        // Support both paginated (.results) and plain array responses
        const items = Array.isArray(data) ? data : data.results || [];
        setActivities(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Activities: fetch error', err);
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

  return (
    <div className="card octofit-card mt-4">
      <div className="card-header bg-dark text-white">
        <h2 className="h4 mb-0">Activities</h2>
      </div>
      <div className="card-body p-0">
        {activities.length === 0 ? (
          <p className="text-muted p-3 mb-0">No activities found.</p>
        ) : (
          <div className="table-responsive">
            <table className="table table-hover table-striped mb-0">
              <thead>
                <tr>
                  <th>User ID</th>
                  <th>Activity Type</th>
                  <th>Duration (min)</th>
                  <th>Calories Burned</th>
                  <th>Date</th>
                  <th>Notes</th>
                </tr>
              </thead>
              <tbody>
                {activities.map((activity, index) => (
                  <tr key={activity._id || index}>
                    <td>{activity.user_id}</td>
                    <td><span className="badge bg-primary">{activity.activity_type}</span></td>
                    <td>{activity.duration}</td>
                    <td>{activity.calories_burned}</td>
                    <td>{activity.date ? new Date(activity.date).toLocaleDateString() : ''}</td>
                    <td>{activity.notes}</td>
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

export default Activities;
