import React from 'react';
import { Line } from 'react-chartjs-2';

const BacktestResults = ({ results }) => {z
    const data = {
        labels: results.map((result, index) => index + 1),
        datasets: [
                {
                    label: 'Backtest Equity Curve',
                    data: results.map(result => result.equity),
                    borderColor: 'blue',
                    fill: false,
                },
            ],
        };
    const options = {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom',
            },
        },
    };

    return (
        <div>
            <h2>Backtest Results</h2>
            <Line data={data} options={options} />
        </div>
    );
};

export default BacktestResults;