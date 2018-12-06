import React from 'react';

const Table = ({ data }) => {
        return (
            <div className="card card-scroll">
            <div className="card-header">
                <h3 className="card-title">Basic Table</h3>
            </div>
            <div className="table-responsive">
                <table className="table card-table table-vcenter text-nowrap">
                    <thead >
                        <tr>
                            <th>ID</th>
                            <th>Start Date</th>
                            <th>Position</th>
                            <th>Education</th>
                            <th>Board</th>
                            <th>Last Date</th>
                            {/* <th>More Info</th>  */}
                        </tr>
                    </thead>
                    <tbody>
                      {
                        data.map((d, i) => {
                            return (
                                <tr> 
                                    <th scope="row">{i}</th>
                                    <td>{d.start_date}</td>
                                    <td>{d.post_name}</td>
                                    <td>{d.education}</td>
                                    <td>{d.requirement_board}</td>
                                    <td>{d.last_date}</td>
                                    {/* <td>{d.more_info}</td>  */}
                                </tr>
                            )
   
                        })
                        }
                    </tbody>
                </table>
            </div>
            <div class="card-body">
                <p className="text-center"><button className='btn-primary-big'>Load More</button></p>
		    </div>
        </div>
        );
    }


export default Table;