import React from 'react';

class Table extends React.Component {
    render(){
        return (
            <div className="card">
            <div className="card-header">
                <h3 className="card-title">Basic Table</h3>
            </div>
            <div className="table-responsive">
                <table className="table card-table table-vcenter text-nowrap">
                    <thead >
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Position</th>
                            <th>Salary</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">1</th>
                            <td>Joan Powell</td>
                            <td>Associate Developer</td>
                            <td>$450,870</td>
                        </tr>
                        <tr>
                            <th scope="row">2</th>
                            <td>Gavin Gibson</td>
                            <td>Account manager</td>
                            <td>$230,540</td>
                        </tr>
                        <tr>
                            <th scope="row">3</th>
                            <td>Julian Kerr</td>
                            <td>Senior Javascript Developer</td>
                            <td>$55,300</td>
                        </tr>
                        <tr>
                            <th scope="row">4</th>
                            <td>Cedric Kelly</td>
                            <td>Accountant</td>
                            <td>$234,100</td>
                        </tr>
                        <tr>
                            <th scope="row">5</th>
                            <td>Samantha May</td>
                            <td>Junior Technical Author</td>
                            <td>$43,198</td>
                        </tr>
                        <tr>
                            <th scope="row">3</th>
                            <td>Julian Kerr</td>
                            <td>Senior Javascript Developer</td>
                            <td>$55,300</td>
                        </tr>
                        <tr>
                            <th scope="row">4</th>
                            <td>Cedric Kelly</td>
                            <td>Accountant</td>
                            <td>$234,100</td>
                        </tr>
                        <tr>
                            <th scope="row">5</th>
                            <td>Samantha May</td>
                            <td>Junior Technical Author</td>
                            <td>$43,198</td>
                        </tr>
                        <tr>
                            <th scope="row">3</th>
                            <td>Julian Kerr</td>
                            <td>Senior Javascript Developer</td>
                            <td>$55,300</td>
                        </tr>
                        <tr>
                            <th scope="row">4</th>
                            <td>Cedric Kelly</td>
                            <td>Accountant</td>
                            <td>$234,100</td>
                        </tr>
                        <tr>
                            <th scope="row">5</th>
                            <td>Samantha May</td>
                            <td>Junior Technical Author</td>
                            <td>$43,198</td>
                        </tr>
                        <tr>
                            <th scope="row">3</th>
                            <td>Julian Kerr</td>
                            <td>Senior Javascript Developer</td>
                            <td>$55,300</td>
                        </tr>
                        <tr>
                            <th scope="row">4</th>
                            <td>Cedric Kelly</td>
                            <td>Accountant</td>
                            <td>$234,100</td>
                        </tr>
                        <tr>
                            <th scope="row">5</th>
                            <td>Samantha May</td>
                            <td>Junior Technical Author</td>
                            <td>$43,198</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        );
    }
}


export default Table;